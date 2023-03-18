import os
import time
import random
import mail_system
import xpaths as x
import pandas as pd
import user_input as ui
import advanced_filter as af
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException


# User Input
job_role = ui.role()
job_location = ui.geo()
job_post_time = ui.listing_time()
experiences = ['Internship', 'Entry level', 'Associate', 'Mid-senior level', 'Director', 'Executive', 'Not applicable']
desired_experience_level = ui.job_level()
no_of_jobs = int(ui.list_length())
advanced_filtering = ui.filtering()
if advanced_filtering:
    maximum_months_of_experience = int(input('Enter the number of months of experience you have: '))


# Setting up webdriver
browser_options = Options()
browser_options.add_experimental_option("detach", True)                                # to prevent browser from closing
os.environ['PATH'] += r'paste path of downloaded webdriver folder'                           # Setting path of webdriver
driver = webdriver.Chrome(options=browser_options)


# Target Website
driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/search?keywords=&location=&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")


# Closing sign-in prompt
try:
    close_sign_in_prompt = WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.XPATH, x.prompt_close())))
    close_sign_in_prompt.click()

except (TimeoutException, NoSuchElementException):
    pass


# SUBMITTING USER INPUT

# -- Entering Title input
job_title_area = driver.find_element(By.XPATH, x.title_box())
job_title_area.send_keys(job_role)                                                   # Entering user input for Job Title
time.sleep(2)

# -- Entering Location Input
location_area = driver.find_element(By.XPATH, x.location_box())
location_area.click()
location_area.clear()
time.sleep(2)
location_area.send_keys(job_location)
time.sleep(2)

search_icon = driver.find_element(By.XPATH, x.search())
search_icon.click()
time.sleep(5)                                                               # Wait time for site reload after submission

# -- Selecting the job listing time
# ---- finding location of Date posted selection filter button from filter menu
match = ['Past 24 hours', 'Past week', 'Past month', 'Any time']                              # To match the xpath texts
listing_time = 'Null'
filter_pos = 1                                         # Storing positing to use it in xpath for selection of user input

for pos in range(1, 7):                          # Looping to match xpath text of each available filter with match array
    dummy_time = WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, x.post_time(pos))))
    if dummy_time.text.strip().capitalize() in match:
        listing_time = dummy_time
        break
    else:
        filter_pos += 1
listing_time.click()
time.sleep(2)

# -- selecting user input
desired_listing_time = 'Null'

for s in range(1, 5):
    select = WebDriverWait(driver, 30).until((ec.element_to_be_clickable((By.XPATH, x.time_selection(filter_pos, s)))))
    if select.text.split('(')[0].strip().capitalize() == job_post_time.strip():
        desired_listing_time = select
        break
    # NOTE: Split function is used as the text are of the form Any Time (24,458)

desired_listing_time.click()
time.sleep(2)
time_done_button = driver.find_element(By.XPATH, x.time_done(filter_pos))
time_done_button.click()


# Advanced Filtering function
def deep_filter():
    try:
        show_more = WebDriverWait(driver, 30).until((ec.element_to_be_clickable((By.XPATH, x.show()))))
        show_more.click()
        job_description = driver.find_element(By.XPATH, x.description()).text

        if len(job_description) == 0:
            return True
        else:
            return af.advanced_filter(job_description, maximum_months_of_experience)
    except TimeoutException:
        return False
    except StaleElementReferenceException:
        time.sleep(4)
        deep_filter()


# Required data:
company_name = []
job_title = []
location = []
experience_level = []
link = []


# Function to add entry in csv
def add_job_detail():
    company_name.append(driver.find_element(By.XPATH, x.company()).text)
    job_title.append(driver.find_element(By.XPATH, x.title()).text)
    location.append(driver.find_element(By.XPATH, x.location()).text)
    experience_level.append(exp_level)
    link.append(job.get_attribute("href"))


# Accessing the jobs title from left pane
i = 1
unexpected_error = 0                                                                        # To avoid any infinite loop

while len(company_name) < no_of_jobs:

    try:
        job = WebDriverWait(driver, 15).until((ec.element_to_be_clickable((By.XPATH, x.jobs(i)))))
        job.click()                                       # Clicking on each job title to open description on right pane

        # Function to click on previous job in case side pane of current selected job doesn't load up
        def timeout_recursion():
            limit = 1
            while limit <= 5:    # Increase loop value in case of slow network or increase the wait time in except block
                try:
                    xp = WebDriverWait(driver, 5).until((ec.element_to_be_clickable((By.XPATH, x.level()))))
                    return xp.text
                except (TimeoutException, StaleElementReferenceException):
                    if i!=1:
                        prev_job = driver.find_element(By.XPATH, x.jobs(i - 1))
                    else:
                        prev_job = driver.find_element(By.XPATH, x.jobs(i + 1))
    
                    prev_job.click()
                    time.sleep(1)
                    job.click()
                    time.sleep(1)
                    limit += 1
                    if limit == 5:
                        print('Poor network connection. Unable to scan one job detail.Bypassing...')
                        return 'Null'
                    continue

        # To find the experience level of the listed job
        try:
            exp_level = timeout_recursion()

        except TimeoutException:
            exp_level = 'Null'
            print('Poor network connection. Unable to scan one job detail.Bypassing...')

        # Matching desired criteria
        if exp_level.strip().capitalize() in desired_experience_level:
            if advanced_filtering:
                if deep_filter():
                    add_job_detail()
                    print(f'{len(company_name)} jobs found from {i} scanned jobs.')
                    unexpected_error = 0
            else:
                add_job_detail()
                unexpected_error = 0

        elif exp_level.strip().capitalize() not in experiences and 'Not applicable' in desired_experience_level and exp_level!= 'Null':
            if advanced_filtering:
                if deep_filter():
                    add_job_detail()
                    print(f'{len(company_name)} jobs found from {i} scanned jobs.')
                    unexpected_error = 0
            else:
                add_job_detail()
                unexpected_error = 0

        i += 1

    except (NoSuchElementException, TimeoutException):

        # Finding if the list has ended by checking existence of listing of job beyond current selection
        try:
            list_end_check = driver.find_element(By.XPATH, x.jobs(i+random.randint(1, 15)))
            # In case this block execute it means list hasn't ended thus skipping current selection and increasing i
            print(f'Unable to locate one Job Title, bypassing...')
            i += 1

        # In case immediate 5th listing cannot be located
        except NoSuchElementException:

            # Checking if the see more jobs button is available
            try:
                see_more_jobs = driver.find_element(By.XPATH, x.show_more())
                see_more_jobs.click()
                time.sleep(5)

            # In case it is not interactable it means the list hasn't ended
            except ElementNotInteractableException:
                print(f'Unable to locate one Job Title, bypassing...')
                unexpected_error += 1
                i += 1

    # To break the loop in case of any unexpected infinite loop error
    if unexpected_error >= 15:
        break


# Exporting as csv file
df = pd.DataFrame({'Company Name': company_name,
                   'Job Title': job_title,
                   'Location': location,
                   'Experience Level': experience_level,
                   'Link': link})

csv_file = df.to_csv(index=False).encode('utf-8')
driver.quit()


# Sending mail
mail_system.mail_sub(csv_file)

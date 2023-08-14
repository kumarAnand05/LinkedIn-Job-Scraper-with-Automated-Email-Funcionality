print("Hold on! Gathering required Files\n")

import os
import time
import random
import mail_system
import xpaths as x
import pandas as pd
import datetime as dt
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
    try:
        maximum_months_of_experience = int(input('Enter the number of months of experience you have: '))
    except ValueError:
        print('Invalid Vlaue entered. Run the script again')
        exit()

# To optimize internet speed (change value in line 94 of user_input.py if internet is too slow)
t = ui.internet_speed()


# To detach web-driver from web browser (to prevent closing)
browser_options = Options()
browser_options.add_experimental_option("detach", False)    # Calling 'add_experimental_option' method from Options class


# Internet Speed Adjustment
very_short_pause = 1 * t
short_pause = 2 * t
long_pause = 5 * t


# Setting path variable for webdriver and creating driver object
os.environ['PATH'] += r'E:/Coding/Projects/LinkedIn Job Scrapper/Selenium Driver'         # Setting path of webdriver
driver = webdriver.Chrome(options=browser_options)                         # Setting which browser is to be automated


# Target Website
driver.maximize_window()                                                               # To maximize the web browser tab
driver.get("https://www.linkedin.com/jobs/search?keywords=&location=&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")


# Closing sign-in prompt
try:
    close_sign_in_prompt = WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.XPATH, x.prompt_close())))
    close_sign_in_prompt.click()                            # The click method clicks on the close_sign_in_prompt object

except (TimeoutException, NoSuchElementException):
    pass


# SUBMITTING USER INPUT

# -- Entering Title input
job_title_area = driver.find_element(By.XPATH, x.title_box())
job_title_area.send_keys(job_role)                                                   # Entering user input for Job Title
time.sleep(short_pause)

# --Entering Location Input
location_area = driver.find_element(By.XPATH, x.location_box())
location_area.click()               # Clicking on input box so that cross button becomes clickable for next line of code
location_area.clear()
time.sleep(short_pause)             # Pausing to mitigate bot detetection

location_area.send_keys(job_location)                                                 # Entering user input for Location
time.sleep(short_pause)

search_icon = driver.find_element(By.XPATH, x.search())
search_icon.click()                                                       # Clicking on search icon to submit user input
time.sleep(long_pause)                                                      # Wait time for site reload after submission

# -- Selecting the job listing time
# ----finding location of Date posted selection filter button from filter menu
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
listing_time.click()                                 # Clicking on time selection filter to expand option to choose from
time.sleep(short_pause)

# -- selecting user input
desired_listing_time = 'Null'
select = 'Null'
networkError = True
availableFilters = []
for s in range(1, 5):
    try:
        select = WebDriverWait(driver, 30).until((ec.element_to_be_clickable((By.XPATH, x.time_selection(filter_pos, s)))))
        networkError=False
        if select.text.split('(')[0].strip().capitalize() == job_post_time.strip():
            desired_listing_time = select
            break
        else:
            availableFilters.append(select.text.split('(')[0].strip().capitalize())
            select = 'Null'
        # NOTE: Split function is used as the text are of the form 'Any Time (24,458)'
    except TimeoutException:
        pass

if select!='Null':
    desired_listing_time.click()                                                                # Clicking on desired option
    time.sleep(short_pause)
    time_done_button = driver.find_element(By.XPATH, x.time_done(filter_pos))
    time_done_button.click()                                                                  # Clicking on the done button

elif networkError == False:
    print(f'Selected job listing time filter is not availabe for the provided Job Title Keyword and Location. Availble Listing Times: {availableFilters}')
    print(f'Please run the script again and select other job listing time or use appropraite Keyword and Location')
    exit()

elif networkError == True:
    print(f'Network problems. Please check your internet connection and run the script again')
    exit()



# Advanced Filtering on
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
        time.sleep(long_pause)
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


# Accessing the jobs title from right pane
i = 1
unexpected_error = 0                                    # To avoid infinite loop if it continuously goes in except block

while len(company_name) < no_of_jobs:                                                        # Number of Jobs to iterate

    try:
        job = WebDriverWait(driver, 15).until((ec.element_to_be_clickable((By.XPATH, x.jobs(i)))))
        job.click()                                       # Clicking on each job title to open description on right pane

        # Function to click on previous job in case side pane of current selected job doesn't load up
        def timeout_recursion():
            limit = 1
            while limit <= long_pause:  # Increase loop value in case of slow network or increase the wait time in except block
                try:
                    xp = WebDriverWait(driver, 5).until((ec.element_to_be_clickable((By.XPATH, x.level()))))
                    return xp.text

                except (TimeoutException, StaleElementReferenceException):
                    if i != 1:
                        prev_job = driver.find_element(By.XPATH, x.jobs(i - 1))
                    else:
                        prev_job = driver.find_element(By.XPATH, x.jobs(i + 1))

                    prev_job.click()
                    time.sleep(very_short_pause)
                    job.click()
                    time.sleep(very_short_pause)
                    limit += 1
                    if limit == long_pause:
                        print('Poor network connection. Unable to scan one job detail. Bypassing...')
                        return 'Null'
                    continue

        # To find the experience level of the listed job
        try:
            exp_level = timeout_recursion()

        except TimeoutException:
            exp_level = 'Null'
            print('Poor network connection. Unable to scan one job detail. Bypassing...')

        # Matching desired criteria
        if exp_level.strip().capitalize() in desired_experience_level:
            unexpected_error = 0
            if advanced_filtering:
                if deep_filter():
                    time.sleep(very_short_pause)
                    add_job_detail()
                    print(f'{len(company_name)} jobs found from {i} scanned jobs.')

            else:
                time.sleep(very_short_pause)
                add_job_detail()

        elif exp_level.strip().capitalize() not in experiences and 'Not applicable' in desired_experience_level and exp_level!= 'Null':
            unexpected_error = 0
            if advanced_filtering:
                if deep_filter():
                    add_job_detail()
                    print(f'{len(company_name)} jobs found from {i} scanned jobs.')
            else:
                add_job_detail()

        i += 1

    except (NoSuchElementException, TimeoutException):

        # Finding if the list has ended by checking existence of listing of job beyond current selection
        try:
            list_end_check = driver.find_element(By.XPATH, x.jobs(i+random.randint(5, 20)))
            # In case this block execute it means list hasn't ended thus skipping current selection and increasing i
            print(f'Unable to locate one Job Title, bypassing...')
            i += 1
            unexpected_error += 0.5

        # In case immediate next listing cannot be located
        except NoSuchElementException:

            # Checking if the see more jobs button is available
            try:
                see_more_jobs = driver.find_element(By.XPATH, x.show_more())
                see_more_jobs.click()
                time.sleep(long_pause)
                i += 1                    # Increasing Value in case see more jobs button available and next listing not interactable
                unexpected_error += 1     # Added in case see more jobs is interactable but doesn't load more jobs

            # In case it is not interactable it means the list has ended
            except ElementNotInteractableException:
                print(f'Unable to locate one Job Title, bypassing...')
                unexpected_error += 1
                i += 1

    # To break the loop in case of any unexpected infinite loop error
    if unexpected_error >= 15:
        break

print('All possible Job data scraped. Browser seesion will close now and data will be stored shortly')

# Exporting as csv file
df = pd.DataFrame({'Company Name': company_name,
                   'Job Title': job_title,
                   'Location': location,
                   'Experience Level': experience_level,
                   'Link': link})

csv_file = df.to_csv(index=False).encode('utf-8')

# To close the web browser at end of the session
driver.quit()

# To save Job Listing on local device (Comment out the line below (Line 288) if you are using mail system feature)
df.to_csv(f'Job Listings {dt.date.today()}.csv', index=False)

# To send Job Listing via mail (Uncomment the line below (Line 291) to enable this feature and set user_mail,passcode and recipent in mail_system.py file.)
# mail_system.mail_sub(csv_file)

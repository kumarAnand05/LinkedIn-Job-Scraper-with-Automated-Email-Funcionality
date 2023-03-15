def prompt_close():
    close_sign_in = '/html/body/div[2]/button'
    return close_sign_in


def title_box():
    title_xpath = '/html/body/div[1]/header/nav/section/section[2]/form/section[1]/input'
    return title_xpath


def location_box():
    location_xpath = '/html/body/div[1]/header/nav/section/section[2]/form/section[2]/input'
    return location_xpath


def search():
    search_icon_xpath = '/html/body/div[1]/header/nav/section/section[2]/form/button'
    return search_icon_xpath


def post_time(pos):
    post_time_button_xpath = f'/html/body/div[1]/section/div/div/div/form/ul/li[{pos}]/div'
    return post_time_button_xpath


def time_selection(filter_pos, s):
    time_selection_option_xpath = f'/html/body/div[1]/section/div/div/div/form/ul/li[{filter_pos}]/div/div/div/div/div/div[{s}]'
    return time_selection_option_xpath


def time_done(filter_pos):
    time_done_button_xpath = f'/html/body/div[1]/section/div/div/div/form/ul/li[{filter_pos}]/div/div/div/button'
    return time_done_button_xpath


def jobs(i):
    listed_job_xpath = f'/html/body/div[1]/div/main/section[2]/ul/li[{i}]/div/a'
    return listed_job_xpath


def level():
    level_xpath = '/html/body/div[1]/div/section/div[2]/div/section[1]/div/ul/li[1]/span'
    return level_xpath


def show():
    show_xpath = '//button[@class="show-more-less-html__button show-more-less-html__button--more"]'
    return show_xpath


def company():
    company_name_xpath = '/html/body/div[1]/div/section/div[2]/section/div/div[1]/div/h4/div[1]/span[1]/a'
    return company_name_xpath


def title():
    job_title_xpath = '/html/body/div[1]/div/section/div[2]/section/div/div[1]/div/a/h2'
    return job_title_xpath


def location():
    location_xpath = '/html/body/div[1]/div/section/div[2]/section/div/div[1]/div/h4/div[1]/span[2]'
    return location_xpath


def description():
    description_xpath = '//div[@class="description__text description__text--rich"]'
    return description_xpath


def show_more():
    show_more_xpath = '//*[@id="main-content"]/section[2]/button'
    return show_more_xpath

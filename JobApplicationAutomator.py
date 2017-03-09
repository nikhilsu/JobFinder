from __future__ import print_function

import getopt
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import JobDetails

def should_run_in_headless_mode():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h', ['headless'])
    except getopt.GetoptError:
        print('invalid options')
    for opt, arg in opts:
        if opt in ('-h', '--headless'):
            return True
    return False


def get_user_input_to_query_jobs():
    global job_category, country, state, city
    print('Job Category : ', end='')
    job_category = raw_input()
    print('Country : ', end='')
    country = raw_input()
    print('State : ', end='')
    state = raw_input()
    print('City : ', end='')
    city = raw_input()


def apply_job_filters():
    job_category_drop_down = Select(driver.find_element_by_name('ac'))
    country_drop_down = Select(driver.find_element_by_name('Country'))
    state_drop_down = Select(driver.find_element_by_name('State'))
    city_drop_down = Select(driver.find_element_by_name('City'))
    job_category_drop_down.select_by_visible_text(job_category)
    country_drop_down.select_by_visible_text(country)
    state_drop_down.select_by_visible_text(state)
    city_drop_down.select_by_visible_text(city)


def wait_till_search_filter_is_applied():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="applied-filters-label"]'))
    )


def display_search_results():
    search_results = driver.find_elements_by_xpath('//*[@id="search-results-list"]/ul/li')
    print("--------------------------------------------------------------------------------")
    print("Job Description \t Job Location")
    print("--------------------------------------------------------------------------------")
    for i in range(1, len(search_results)):
        job_description = driver.find_element_by_xpath('//*[@id="search-results-list"]/ul/li[' + str(i) + ']/a/h2').text
        job_location = driver.find_element_by_xpath('//*[@id="search-results-list"]/ul/li[' + str(i) + ']/span').text
        print(job_description + '\t' + job_location)
    print("--------------------------------------------------------------------------------")


if __name__ == "__main__":
    if should_run_in_headless_mode():
        driver = webdriver.PhantomJS()
        driver.set_window_size(1280, 720)
    else:
        driver = webdriver.Chrome()

    driver.get("https://h30631.www3.hp.com/search-jobs")

    job_detail = JobDetails.JobDetails(driver)
    job_detail.display_details()

    try:
        get_user_input_to_query_jobs()
        apply_job_filters()

        driver.find_element_by_xpath("//button[text()='Search']").click()
        wait_till_search_filter_is_applied()

        display_search_results()

    except Exception as e:
        print(e)
        print('No Jobs found')
    finally:
        driver.close()

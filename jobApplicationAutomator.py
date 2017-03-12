from __future__ import print_function
from selenium import webdriver
from jobFilters import JobFilters
from jobFinder import JobFinder
from jobQueryParameters import JobQueryParameters
import getopt
import sys


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
    print('Job Category : ', end='')
    job_category = raw_input()
    print('Country : ', end='')
    country = raw_input()
    print('State : ', end='')
    state = raw_input()
    print('City : ', end='')
    city = raw_input()
    return JobQueryParameters(job_category, country, state, city)


def display_job_results(jobs):
    delimiter = ' |\t '

    print("--------------------------------------------------------------------------------")
    print("Sl.No." + delimiter + "Job Description" + delimiter + "Job Location" + delimiter + "Web Link")
    print("--------------------------------------------------------------------------------")
    for index, job in enumerate(jobs):
        print(str(index) + delimiter + job.description + delimiter + job.location + delimiter + job.web_link)
    print("--------------------------------------------------------------------------------")


if __name__ == "__main__":
    if should_run_in_headless_mode():
        driver = webdriver.PhantomJS()
        driver.set_window_size(1280, 720)
    else:
        driver = webdriver.Chrome()

    driver.get("https://h30631.www3.hp.com/search-jobs")

    job_filters = JobFilters(driver)
    job_filters.display_filters()

    try:
        job_finder = JobFinder(driver, get_user_input_to_query_jobs())
        display_job_results(job_finder.fetch_results())

    except Exception as e:
        print(e)
        print('No Jobs found')
    finally:
        driver.close()

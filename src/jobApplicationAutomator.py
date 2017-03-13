from __future__ import print_function
from selenium import webdriver
from jobFilters import JobFiltersCollector
from jobFinder import JobFinder
from jobApplication import JobApplication
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
    job_category = raw_input('Job Category : ')
    country = raw_input('Country : ')
    state = raw_input('State : ')
    city = raw_input('City : ')
    return JobQueryParameters(job_category, country, state, city)


def display_job_results(jobs):
    delimiter = ' |\t '

    print('--------------------------------------------------------------------------------')
    print('Sl.No.' + delimiter + 'Job Description' + delimiter + 'Job Location' + delimiter + 'Web Link')
    print('--------------------------------------------------------------------------------')
    for index, job in enumerate(jobs):
        print(str(index) + delimiter + job.description + delimiter + job.location + delimiter + job.web_link)
    print('--------------------------------------------------------------------------------')


def display_filters(filters):
    print("\n\nJob Categories :-")
    for job_category in filters.job_categories:
        print(job_category)

    print("\n\nCountries :-")
    for country in filters.countries:
        print(country)

    print("\n\nStates :-")
    for state in filters.states:
        print(state)

    print("\n\nCities :-")
    for city in filters.cities:
        print(city)


if __name__ == "__main__":
    if should_run_in_headless_mode():
        driver = webdriver.PhantomJS()
        driver.set_window_size(1280, 720)
    else:
        driver = webdriver.Chrome()

    driver.get('https://h30631.www3.hp.com/search-jobs')

    job_filters = JobFiltersCollector(driver).fetch_filters()
    display_filters(job_filters)

    try:
        job_finder = JobFinder(driver, get_user_input_to_query_jobs())
        job_results = job_finder.fetch_results()
        display_job_results(job_results)
        job_index = int(raw_input('Enter Sl.No of Job to apply for : '))
        if job_index in range(1, len(job_results)):
            job_application = JobApplication(driver, job_results[job_index])
            job_application.apply()
        else:
            raise Exception('Invalid job chosen')

    except Exception as e:
        print(e)
        print('No Jobs found')
    finally:
        driver.close()

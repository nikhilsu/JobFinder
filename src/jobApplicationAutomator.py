from __future__ import print_function

import getopt
import sys

from selenium import webdriver

from answers import Answers
from applicationQuestionsPage import ApplicationQuestionsPage
from createAccountPage import CreateAccountPage
from inputOutput import InputOutput, JobOutput
from jobApplication import JobApplication
from jobFilter import JobFilter
from jobFinder import JobFinder
from myInformationPage import MyInformationPage
from user import User


def should_run_in_headless_mode():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h', ['headless'])
    except getopt.GetoptError:
        print('invalid options')
    for opt, arg in opts:
        if opt in ('-h', '--headless'):
            return True
    return False


def get_all_job_filters():
    return [JobFilter(driver, 'ac', 'Job Category'),
            JobFilter(driver, 'Country', 'Country'),
            JobFilter(driver, 'State', 'State'),
            JobFilter(driver, 'City', 'City')]


if __name__ == "__main__":
    if should_run_in_headless_mode():
        driver = webdriver.PhantomJS()
        driver.set_window_size(1280, 720)
    else:
        driver = webdriver.Chrome()

    driver.get('https://h30631.www3.hp.com/search-jobs')

    try:
        job_finder = JobFinder(driver, get_all_job_filters())
        job_results = job_finder.fetch_results()
        JobOutput.tabular_display(job_results)
        job_index = int(InputOutput.input('Enter Sl.No of Job to apply for : '))
        if job_index in range(0, len(job_results)):
            email_address = InputOutput.input('Email address : ')
            first_name = InputOutput.input('First Name : ')
            last_name = InputOutput.input('Last Name : ')
            phone_number = InputOutput.get_valid_phone_number()
            user = User(first_name, last_name, phone_number, email_address, InputOutput.get_valid_password())
            create_account_page = CreateAccountPage(driver, user)
            my_information_page = MyInformationPage(driver, user)
            answers = Answers(True, True, True, True, True, ["India"], True, True)
            application_questions_page = ApplicationQuestionsPage(driver, answers)
            job_application = JobApplication(driver, job_results[job_index], user, create_account_page,
                                             my_information_page, application_questions_page)
            job_application.apply()
        else:
            raise Exception('Invalid job chosen')

    except Exception as e:
        InputOutput.output(e)
        InputOutput.output('No Jobs found')
    finally:
        driver.close()

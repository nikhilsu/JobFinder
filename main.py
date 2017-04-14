from __future__ import print_function

import getopt
import sys

from selenium import webdriver
from src.controller.jobApplication import JobApplication
from src.controller.jobFilter import JobFilter
from src.controller.jobFinder import JobFinder
from src.helper.inputOutput import InputOutput, JobOutput
from src.model.answers import Answers
from src.model.pages.applicationQuestionsPage import ApplicationQuestionsPage
from src.model.pages.createAccountPage import CreateAccountPage
from src.model.pages.myExperiencePage import MyExperiencePage
from src.model.pages.myInformationPage import MyInformationPage
from src.model.pages.selfIdentityPage import SelfIdentityPage
from src.model.pages.voluntaryDisclosuresPage import VoluntaryDisclosuresPage
from src.model.user import User


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


def build_pages():
    create_account_page = CreateAccountPage(driver, user)
    my_information_page = MyInformationPage(driver, user)
    my_experience_page = MyExperiencePage(driver)
    application_questions_page = ApplicationQuestionsPage(driver, answers)
    voluntary_disclosures_page = VoluntaryDisclosuresPage(driver, user.gender)
    self_identity_page = SelfIdentityPage(driver, user.full_name())

    return [create_account_page, my_information_page, my_experience_page,
            application_questions_page, voluntary_disclosures_page, self_identity_page]


def set_console_size(rows, columns):
    sys.stdout.write("\x1b[8;{0};{1}t".format(rows, columns))


if __name__ == "__main__":
    set_console_size(80, 250)

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
            gender = InputOutput.input('Gender', ['Male', 'Female', 'Undeclared'])
            user = User(first_name, last_name, phone_number, email_address, InputOutput.get_valid_password(), gender)
            answers = Answers(True, True, True, True, True, ["India"], True, True)

            job_application = JobApplication(driver, job_results[job_index], user, build_pages())
            job_application.apply()
        else:
            raise Exception('Invalid job chosen')

    except Exception as e:
        InputOutput.output(e)
        InputOutput.output('No Jobs found')
    finally:
        driver.close()

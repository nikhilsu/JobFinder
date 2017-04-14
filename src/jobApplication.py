from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class JobApplication(object):
    def __init__(self, driver, job, user, create_account_page, my_information_page, application_questions_page):
        self.application_questions_page = application_questions_page
        self.my_information_page = my_information_page
        self.create_account_page = create_account_page
        self.driver = driver
        self.job = job
        self.user = user

    def apply(self):
        self.driver.get(self.job.web_link)
        self.driver.find_element_by_link_text('Apply').click()
        self.driver.find_element_by_name('FirstName').send_keys(self.user.first_name)
        self.driver.find_element_by_name('LastName').send_keys(self.user.last_name)
        self.driver.find_element_by_name('EmailAddress').send_keys(self.user.email_address)
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        self.__wait_till_login_form_is_visible()
        self.create_account_page.create()
        self.__wait_and_click_next_button_on_first_page()
        self.__wait_for_page_to_load('My Information')
        self.my_information_page.fill()
        self.__click_next_button()
        self.__wait_for_page_to_load('Application Questions')
        self.application_questions_page.fill()
        self.__click_next_button()

        print('Job application form is open in the web driver. Fill in the details to apply!')

    def __wait_and_click_next_button_on_first_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="vpsBody"]/div[6]/div[1]/div[1]/button[1]'))
        )
        self.driver.find_element_by_xpath('//*[@id="vpsBody"]/div[6]/div[1]/div[1]/button[1]').click()

    def __wait_till_login_form_is_visible(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-automation-id='goButton']")))

    def __wait_for_page_to_load(self, page_name):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="wd-WizardPage-wizardView"]/div[1]/div[1]/span'),
                                             page_name))

    def __click_next_button(self):
        self.driver.find_element_by_xpath('//*[@id="vpsBody"]/div[6]/div[1]/div[2]/button[1]').click()

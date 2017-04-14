from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.model.pages.page import Page


class CreateAccountPage(Page):
    def __init__(self, driver, name, user):
        super(CreateAccountPage, self).__init__(driver, name)
        self.user = user

    def __click_next_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="vpsBody"]/div[6]/div[1]/div[1]/button[1]'))
        )
        self.driver.find_element_by_xpath('//*[@id="vpsBody"]/div[6]/div[1]/div[1]/button[1]').click()

    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-automation-id='goButton']")))

    def fill(self):
        self.driver.find_element_by_xpath(
            '//*[@id="wd-Authentication-authentication"]/div/div/div[2]/div/div[6]/div/div[1]/a').click()
        self.driver.find_element_by_xpath(
            '//div[@data-automation-id="userName"]/input[@type="text"]').send_keys(self.user.email_address)
        self.driver.find_element_by_xpath(
            '//div[@data-automation-id="password"]/input[@type="password"]').send_keys(self.user.password)
        self.driver.find_element_by_xpath(
            '//div[@data-automation-id="confirmPassword"]/input[@type="password"]').send_keys(self.user.password)
        self.driver.find_element_by_xpath(
            '//div[@data-automation-id="confirmPassword"]/input[@type="password"]').send_keys(Keys.RETURN)
        self.__click_next_button()

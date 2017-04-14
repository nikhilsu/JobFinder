from abc import ABCMeta, abstractmethod
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Page(object):
    __metaclass__ = ABCMeta

    def __init__(self, driver, name):
        self.driver = driver
        self.name = name

    @abstractmethod
    def fill(self):
        return

    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="wd-WizardPage-wizardView"]/div[1]/div[1]/span'),
                                             self.name))

    def click_next_button(self):
        next_button = self.driver.find_element_by_xpath('//*[@id="vpsBody"]/div[6]/div[1]/div[2]/button[1]')
        self.driver.execute_script('arguments[0].click();', next_button)

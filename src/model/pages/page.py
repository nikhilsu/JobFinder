from abc import ABCMeta, abstractmethod
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.helper.timer import Timer


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
        self.try_and_click(next_button)

    def select_option_from_drop_down(self, option, drop_down):
        self.try_and_click(drop_down)
        Timer.sleep()
        drop_down_element = self.driver.find_element_by_xpath('//div[@data-automation-label="{0}"]/../../..'
                                                              .format(option))
        self.try_and_click(drop_down_element)
        Timer.sleep()

    def try_and_click(self, element):
        # noinspection PyBroadException
        try:
            element.click()
        except:
            self.driver.execute_script('arguments[0].click();', element)


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class JobApplication(object):
    def __init__(self, driver, job):
        self.driver = driver
        self.job = job

    def apply(self):
        self.driver.get(self.job.web_link)
        self.__wait_till_apply_button_is_visible()
        self.driver.find_element_by_link_text('Apply').click()
        print('Job application form is open in the web driver. Fill in the details to apply!')

    def __wait_till_apply_button_is_visible(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Apply']"))
        )

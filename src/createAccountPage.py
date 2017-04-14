from selenium.webdriver.common.keys import Keys


class CreateAccountPage(object):
    def __init__(self, driver, user):
        self.driver = driver
        self.user = user

    def create(self):
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

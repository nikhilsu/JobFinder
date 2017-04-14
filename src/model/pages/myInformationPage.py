from src.model.pages.page import Page


class MyInformationPage(Page):
    def __init__(self, driver, name, user):
        super(MyInformationPage, self).__init__(driver, name)
        self.user = user

    def fill(self):
        self.driver.find_element_by_xpath(
            '//*[@id="textInput.nameComponent--uid12-input"]').send_keys(self.user.first_name)
        self.driver.find_element_by_xpath(
            '//*[@id="textInput.nameComponent--uid13-input"]').send_keys(self.user.last_name)
        self.driver.find_element_by_xpath(
            '//*[@id="textInput.phone--uid19-input"]').send_keys(self.user.phone_number)
        self.driver.find_element_by_xpath('//*[@id="dropDownSelectList.sources-input--uid20-input"]/div[1]/div').click()
        drop_down_element = self.driver.find_element_by_xpath('//div[@id="dropDownSelectList.sources-input-entry-3"]')
        self.driver.execute_script("arguments[0].click();", drop_down_element)
        self.driver.find_element_by_xpath('//button[@data-automation-id="wd-CommandButton_next"]').click()
        super(MyInformationPage, self).click_next_button()

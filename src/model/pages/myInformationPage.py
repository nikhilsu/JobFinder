from src.helper.timer import Timer
from src.model.pages.page import Page


class MyInformationPage(Page):
    def __init__(self, driver, user):
        super(MyInformationPage, self).__init__(driver, 'My Information')
        self.user = user

    def fill(self):
        base = super(MyInformationPage, self)
        self.driver.find_element_by_xpath(
            '//*[@id="textInput.nameComponent--uid12-input"]').send_keys(self.user.first_name)
        Timer.sleep()
        self.driver.find_element_by_xpath(
            '//*[@id="textInput.nameComponent--uid13-input"]').send_keys(self.user.last_name)
        Timer.sleep()
        self.driver.find_element_by_xpath(
            '//*[@id="textInput.phone--uid19-input"]').send_keys(self.user.phone_number)
        self.driver.find_element_by_xpath('//*[@id="dropDownSelectList.sources-input--uid20-input"]/div[1]/div').click()
        Timer.sleep()
        drop_down_element = self.driver.find_element_by_xpath('//div[@id="dropDownSelectList.sources-input-entry-3"]')
        base.try_and_click(drop_down_element)
        Timer.sleep()
        self.driver.find_element_by_xpath('//button[@data-automation-id="wd-CommandButton_next"]').click()
        Timer.sleep()
        base.click_next_button()

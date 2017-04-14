class JobApplication(object):
    def __init__(self, driver, job, user, pages):
        self.driver = driver
        self.job = job
        self.user = user
        self.pages = pages

    def apply(self):
        self.driver.get(self.job.web_link)
        self.driver.find_element_by_link_text('Apply').click()
        self.driver.find_element_by_name('FirstName').send_keys(self.user.first_name)
        self.driver.find_element_by_name('LastName').send_keys(self.user.last_name)
        self.driver.find_element_by_name('EmailAddress').send_keys(self.user.email_address)
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        for page in self.pages:
            page.wait_for_page_to_load()
            page.fill()
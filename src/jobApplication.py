class JobApplication(object):
    def __init__(self, driver, job):
        self.driver = driver
        self.job = job

    def apply(self):
        # self.driver.find_element_by_xpath(
        # '//*[@id="search-results-list"]/ul/li/a[@href="' + self.job.web_link + '"]').click()
        self.driver.get(self.job.web_link)
        print('Job application form is open in the web driver. Fill in the details to apply!')

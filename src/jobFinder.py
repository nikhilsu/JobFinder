from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from job import Job


class JobFinder:
    def __init__(self, driver, job_filters):
        self.job_filters = job_filters
        self.driver = driver

    def __apply_job_filters(self):
        for f in self.job_filters:
            f.apply_filter()

    def __wait_till_search_filter_is_applied(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="applied-filters-label"]'))
        )

    def fetch_results(self):
        self.__apply_job_filters()
        self.driver.find_element_by_xpath("//button[text()='Search']").click()
        self.__wait_till_search_filter_is_applied()

        search_results = self.driver.find_elements_by_xpath('//*[@id="search-results-list"]/ul/li')
        jobs = []
        for i in range(1, len(search_results)):
            job_description = self.driver.find_element_by_xpath(
                '//*[@id="search-results-list"]/ul/li[' + str(i) + ']/a/h2').text
            job_location = self.driver.find_element_by_xpath(
                '//*[@id="search-results-list"]/ul/li[' + str(i) + ']/span').text
            job_web_link = self.driver.find_element_by_xpath(
                '//*[@id="search-results-list"]/ul/li[' + str(i) + ']/a').get_attribute("href")
            job = Job(job_description, job_location, job_web_link)
            jobs.append(job)
        return jobs

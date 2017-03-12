from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from job import Job


class JobFinder:
    def __init__(self, driver, job_search_parameters):
        self.job_query_parameters = job_search_parameters
        self.driver = driver

    def __apply_job_filters(self):
        job_category_drop_down = Select(self.driver.find_element_by_name('ac'))
        country_drop_down = Select(self.driver.find_element_by_name('Country'))
        state_drop_down = Select(self.driver.find_element_by_name('State'))
        city_drop_down = Select(self.driver.find_element_by_name('City'))
        job_category_drop_down.select_by_visible_text(self.job_query_parameters.job_category)
        country_drop_down.select_by_visible_text(self.job_query_parameters.country)
        state_drop_down.select_by_visible_text(self.job_query_parameters.state)
        city_drop_down.select_by_visible_text(self.job_query_parameters.city)

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

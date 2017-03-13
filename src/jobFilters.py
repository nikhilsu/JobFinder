from selenium.webdriver.support.ui import Select


class JobFiltersCollector:
    def __init__(self, driver):
        self.driver = driver

    def fetch_filters(self):
        job_categories = self.__fetch_filters_from_drop_down('ac')
        countries = self.__fetch_filters_from_drop_down('Country')
        states = self.__fetch_filters_from_drop_down('State')
        cities = self.__fetch_filters_from_drop_down('City')
        return JobFilters(job_categories, countries, states, cities)

    def __fetch_filters_from_drop_down(self, drop_down_name):
        return [option.text for option in Select(self.driver.find_element_by_name(drop_down_name)).options]


class JobFilters:
    def __init__(self, job_categories, countries, states, cities):
        self.job_categories = job_categories
        self.countries = countries
        self.states = states
        self.cities = cities

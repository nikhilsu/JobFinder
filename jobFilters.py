from selenium.webdriver.support.ui import Select


class JobFilters:
    def __init__(self, driver):
        self.driver = driver

    def display_filters(self):
        job_categories_options = Select(self.driver.find_element_by_name('ac')).options
        countries_options = Select(self.driver.find_element_by_name('Country')).options
        states_options = Select(self.driver.find_element_by_name('State')).options
        cities_options = Select(self.driver.find_element_by_name('City')).options

        print("\n\nJob Categories :-")
        for job_category in job_categories_options:
            print (job_category.text)

        print("\n\nCountries :-")
        for country in countries_options:
            print (country.text)

        print("\n\nStates :-")
        for state in states_options:
            print (state.text)

        print("\n\nCities :-")
        for city in cities_options:
            print (city.text)

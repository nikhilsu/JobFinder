import time
from selenium.webdriver.support.ui import Select
from inputOutput import InputOutput

from inputOutput import Color


class JobFilter(object):
    def __init__(self, driver, filter_drop_down_name, filter_name):
        self.driver = driver
        self.filter_drop_down_name = filter_drop_down_name
        self.filter_name = filter_name

    def apply_filter(self):
        filter_values_options = Select(self.driver.find_element_by_name(self.filter_drop_down_name)).options
        InputOutput.output('\n\n' + Color.UNDERLINE + Color.BOLD + self.filter_name + Color.END + Color.END + ' :-\n')
        self.__print_filter_values_in_drop_down(filter_values_options)
        user_choice = int(InputOutput.input('\nEnter ' + self.filter_name + ' : '))
        while True:
            if user_choice in range(0, len(filter_values_options)):
                filter_value = filter_values_options[user_choice].text
                Select(self.driver.find_element_by_name(self.filter_drop_down_name)) \
                    .select_by_visible_text(filter_value)
                self.__wait_till_other_filter_drop_downs_refresh()
                break
            else:
                user_choice = int(InputOutput.input('Invalid choice. Enter again : '))

    @staticmethod
    def __wait_till_other_filter_drop_downs_refresh():
        time.sleep(2)

    @staticmethod
    def __print_filter_values_in_drop_down(options):
        for index, option in enumerate(options):
            InputOutput.output(str(index) + '. ' + str(option.text))

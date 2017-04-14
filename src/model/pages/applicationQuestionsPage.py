from src.helper.timer import Timer
from src.model.pages.page import Page


class ApplicationQuestionsPage(Page):
    def __init__(self, driver, name, answers):
        super(ApplicationQuestionsPage, self).__init__(driver, name)
        self.answers = answers

    def fill(self):
        answer_drop_downs = self.driver.find_elements_by_xpath('//div[@data-automation-id="selectSelectedOption"]')

        first_answer = self.__get_answer(self.answers.first_answer)
        self.__select_option_from_drop_down(first_answer, answer_drop_downs[0])

        second_answer = self.__get_answer(self.answers.second_answer)
        self.__select_option_from_drop_down(second_answer, answer_drop_downs[1])

        third_answer = self.__get_answer(self.answers.third_answer)
        self.__select_option_from_drop_down(third_answer, answer_drop_downs[2])

        fourth_answer = self.__get_answer(self.answers.fourth_answer)
        self.__select_option_from_drop_down(fourth_answer, answer_drop_downs[3])

        fifth_answer = self.__get_answer(self.answers.fifth_answer)
        self.__select_option_from_drop_down(fifth_answer, answer_drop_downs[4])

        sixth_country_answer = ' '.join(self.answers.countries_been_in)
        self.driver.find_element_by_xpath('//textarea[@data-automation-id="textAreaField"]') \
            .send_keys(sixth_country_answer)

        seventh_answer = self.__get_answer(self.answers.seventh_answer)
        self.__select_option_from_drop_down(seventh_answer, answer_drop_downs[5])

        eighth_answer = self.__get_answer(self.answers.eighth_answer)
        self.__select_option_from_drop_down(eighth_answer, answer_drop_downs[6])

        super(ApplicationQuestionsPage, self).click_next_button()

    def __select_option_from_drop_down(self, first_answer, drop_down):
        # noinspection PyBroadException
        try:
            drop_down.click()
        except:
            self.driver.execute_script('arguments[0].click();', drop_down)
        Timer.sleep()
        drop_down_element = self.driver.find_element_by_xpath('//div[@data-automation-label="{0}"]/../../..'
                                                              .format(first_answer))
        self.driver.execute_script('arguments[0].click();', drop_down_element)
        Timer.sleep()

    @staticmethod
    def __get_answer(answer):
        return 'Yes' if answer else 'No'

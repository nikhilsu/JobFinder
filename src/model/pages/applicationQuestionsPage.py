from src.model.pages.page import Page


class ApplicationQuestionsPage(Page):
    def __init__(self, driver, answers):
        super(ApplicationQuestionsPage, self).__init__(driver, 'Application Questions')
        self.answers = answers

    def fill(self):
        base = super(ApplicationQuestionsPage, self)

        answer_drop_downs = self.driver.find_elements_by_xpath('//div[@data-automation-id="selectSelectedOption"]')

        first_answer = self.__get_answer(self.answers.first_answer)
        base.select_option_from_drop_down(first_answer, answer_drop_downs[0])

        second_answer = self.__get_answer(self.answers.second_answer)
        base.select_option_from_drop_down(second_answer, answer_drop_downs[1])

        third_answer = self.__get_answer(self.answers.third_answer)
        base.select_option_from_drop_down(third_answer, answer_drop_downs[2])

        fourth_answer = self.__get_answer(self.answers.fourth_answer)
        base.select_option_from_drop_down(fourth_answer, answer_drop_downs[3])

        fifth_answer = self.__get_answer(self.answers.fifth_answer)
        base.select_option_from_drop_down(fifth_answer, answer_drop_downs[4])

        sixth_country_answer = ' '.join(self.answers.countries_been_in)
        self.driver.find_element_by_xpath('//textarea[@data-automation-id="textAreaField"]') \
            .send_keys(sixth_country_answer)

        seventh_answer = self.__get_answer(self.answers.seventh_answer)
        base.select_option_from_drop_down(seventh_answer, answer_drop_downs[5])

        eighth_answer = self.__get_answer(self.answers.eighth_answer)
        base.select_option_from_drop_down(eighth_answer, answer_drop_downs[6])

        base.click_next_button()

    @staticmethod
    def __get_answer(answer):
        return 'Yes' if answer else 'No'

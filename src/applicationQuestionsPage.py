class ApplicationQuestionsPage(object):
    def __init__(self, driver, answers):
        self.driver = driver
        self.answers = answers

    def fill(self):
        first_answer = self.__get_answer(self.answers.first_answer)
        self.__select_option_from_drop_down(first_answer, '//*[@id=\"wd-FieldSet-NO_METADATA_ID-uid122\"]/div['
                                                          '2]/div/ul/li/div[2]/div/div[1]/div')
        second_answer = self.__get_answer(self.answers.second_answer)
        self.__select_option_from_drop_down(second_answer, '//*[@id="wd-FieldSet-NO_METADATA_ID-uid124"]/div['
                                                           '2]/div/ul/li/div[2]/div/div[1]/div')
        third_answer = self.__get_answer(self.answers.third_answer)
        self.__select_option_from_drop_down(third_answer, '//*[@id="wd-FieldSet-NO_METADATA_ID-uid126"]/div['
                                                          '2]/div/ul/li/div[2]/div/div[1]/div')

        fourth_answer = self.__get_answer(self.answers.fourth_answer)
        self.__select_option_from_drop_down(fourth_answer, '//*[@id="wd-FieldSet-NO_METADATA_ID-uid128"]/div['
                                                           '2]/div/ul/li/div[2]/div/div[1]/div')

        fifth_answer = self.__get_answer(self.answers.fifth_answer)
        self.__select_option_from_drop_down(fifth_answer, '//*[@id="wd-FieldSet-NO_METADATA_ID-uid130"]/div['
                                                          '2]/div/ul/li/div[2]/div/div[1]/div')

        sixth_country_answer = ' '.join(self.answers.countries_been_in)
        self.driver.find_element_by_xpath('//textarea[@data-automation-id="textAreaField"]') \
            .send_keys(sixth_country_answer)

        seventh_answer = self.__get_answer(self.answers.seventh_answer)
        self.__select_option_from_drop_down(seventh_answer, '//*[@id="wd-FieldSet-NO_METADATA_ID-uid45"]/div['
                                                            '2]/div/ul/li/div[2]/div')

        eighth_answer = self.__get_answer(self.answers.eighth_answer)
        self.__select_option_from_drop_down(eighth_answer, '//*[@id="wd-FieldSet-NO_METADATA_ID-uid45"]/div['
                                                           '2]/div/ul/li/div[2]/div')

    def __select_option_from_drop_down(self, first_answer, drop_down):
        self.driver.find_element_by_xpath(drop_down).click()
        drop_down_element = self.driver.find_element_by_xpath('//div[@data-automation-label="{0}"]/../../..'
                                                              .format(first_answer))
        self.driver.execute_script("arguments[0].click();", drop_down_element)

    @staticmethod
    def __get_answer(answer):
        return 'Yes' if answer else 'No'

from src.helper.inputOutput import InputOutput
from src.model.pages.page import Page


class VoluntaryDisclosuresPage(Page):
    def __init__(self, driver, gender):
        super(VoluntaryDisclosuresPage, self).__init__(driver, 'Voluntary Disclosures')
        self.gender = gender

    def fill(self):
        base = super(VoluntaryDisclosuresPage, self)
        drop_downs = self.driver.find_elements_by_xpath('//div[@data-automation-id="selectSelectedOption"]')

        gender_selection_drop_down = drop_downs[0]
        base.select_option_from_drop_down(self.gender, gender_selection_drop_down)

        check_boxes = self.driver.find_elements_by_xpath('//div[@data-automation-id="checkboxPanel"]')
        InputOutput.output('Are you? :-')
        for check_box in check_boxes:
            check_box_text = check_box.find_element_by_xpath('../label').text
            if check_box_text == '' or InputOutput.input_yes_no(check_box_text):
                base.try_and_click(check_box)

        military_veteran_drop_down = drop_downs[1]
        base.select_option_from_drop_down('I AM NOT A VETERAN', military_veteran_drop_down)

        base.click_next_button()

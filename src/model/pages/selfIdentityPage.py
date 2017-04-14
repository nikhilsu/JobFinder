import time

from selenium.webdriver import ActionChains

from src.helper.inputOutput import InputOutput
from src.helper.timer import Timer
from src.model.pages.page import Page


class SelfIdentityPage(Page):
    def __init__(self, driver, full_name):
        super(SelfIdentityPage, self).__init__(driver, 'Self Identify')
        self.full_name = full_name

    def fill(self):
        base = super(SelfIdentityPage, self)

        check_boxes = self.driver.find_elements_by_xpath('//div[@data-automation-id="checkboxPanel"]')
        answer = InputOutput.input_yes_no('\n\nDo you wish to answer a question on your disability(/ies), if any?')
        if not answer:
            base.try_and_click(check_boxes[2])
        else:
            InputOutput.output("How do I know if I have a disability?\nYou are considered to have a disability if "
                               "you have a physical or mental impairment or medical condition that substantially "
                               "limits a major life activity, or if you have a history or record of such an "
                               "impairment or medical condition.\nDisabilities include, but are not limited to: \n- "
                               "Blindness\n- Deafness\n- Cancer\n- Diabetes\n- Epilepsy\n- Autism\n- Cerebral "
                               "palsy\n- HIV/AIDS\n- Schizophrenia\n- Muscular dystrophy\n- Bipolar disorder\n- "
                               "Major depression\n- Multiple sclerosis (MS)\n- Missing limbs or partially missing "
                               "limbs\n- Post-traumatic stress disorder (PTSD)\n- Obsessive compulsive disorder\n- "
                               "Impairments requiring the use of a wheelchair\n- Intellectual disability ("
                               "previously called mental retardation)")
            disabilities_answer = InputOutput.input_yes_no('Do you have or have had any of the above disabilities?')
            if disabilities_answer:
                base.try_and_click(check_boxes[0])
            else:
                base.try_and_click(check_boxes[1])

        self.driver.find_element_by_xpath('(//div[@data-automation-id="textInput"])[6]/input').send_keys(self.full_name)

        Timer.sleep()

        base.try_and_click(self.driver.find_element_by_xpath('//span[@data-automation-id="dateSectionMonth"]'))
        ActionChains(self.driver).send_keys(time.strftime("%m%d%Y")).perform()

        base.click_next_button()

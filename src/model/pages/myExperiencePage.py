from src.model.pages.page import Page


class MyExperiencePage(Page):
    def __init__(self, driver):
        super(MyExperiencePage, self).__init__(driver, 'My Experience')

    def fill(self):
        super(MyExperiencePage, self).click_next_button()

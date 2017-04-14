from src.model.pages.page import Page


class MyExperiencePage(Page):
    def __init__(self, driver, name):
        super(MyExperiencePage, self).__init__(driver, name)

    def fill(self):
        super(MyExperiencePage, self).click_next_button()

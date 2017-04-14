from src.model.pages.page import Page


class ReviewPage(Page):
    def __init__(self, driver):
        super(ReviewPage, self).__init__(driver, 'Review')

    def fill(self):
        super(ReviewPage, self).click_next_button()
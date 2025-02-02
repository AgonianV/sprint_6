from pages.base_page import BasePageScooter

class MainPageScooter(BasePageScooter):
    def __init__(self, driver, f_locator, s_locator):
        super().__init__(driver, f_locator, s_locator)

    def check_answer_on_question(self):
        self.scroll_footter()
        self.click_on_question()
        self.wait_for_load_answer()




from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import *

class MainPageScooter:
    first_button = [By.XPATH, first_question_button]
    first_answer = [By.XPATH, first_question_answer]

    second_button = [By.XPATH, second_question_button]
    second_answer = [By.XPATH, second_question_answer]

    third_button = [By.XPATH, third_question_button]
    third_answer = [By.XPATH, third_question_answer]

    fourth_button = [By.XPATH, fourth_question_button]
    fourth_answer = [By.XPATH, fourth_question_answer]

    fifth_button = [By.XPATH, fifth_question_button]
    fifth_answer = [By.XPATH, fifth_question_answer]

    sixth_button = [By.XPATH, sixth_question_button]
    sixth_answer = [By.XPATH, sixth_question_answer]

    seventh_button = [By.XPATH, seventh_question_button]
    seventh_answer = [By.XPATH, seventh_question_answer]

    eighth_button = [By.XPATH, eighth_question_button]
    eighth_answer = [By.XPATH, eighth_question_answer]

    def __init__(self, driver, f_locator, s_locator):
        self.driver = driver
        self.f_locator = f_locator
        self.s_locator = s_locator
    def click_on_question(self):
        self.driver.find_element(*self.f_locator).click()

    def answer_on_question(self):
        return self.driver.find_element(*self.s_locator).text

    def wait_for_load_answer(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.s_locator))

    def scroll_footter(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


    def check_answer_on_question(self):
        self.scroll_footter()
        self.click_on_question()
        self.wait_for_load_answer()




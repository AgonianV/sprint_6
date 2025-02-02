from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import *
import allure

class BasePageScooter:
    first_button = [By.ID, first_question_button]
    first_answer = [By.ID, first_question_answer]

    second_button = [By.ID, second_question_button]
    second_answer = [By.ID, second_question_answer]

    third_button = [By.ID, third_question_button]
    third_answer = [By.ID, third_question_answer]

    fourth_button = [By.ID, fourth_question_button]
    fourth_answer = [By.ID, fourth_question_answer]

    fifth_button = [By.ID, fifth_question_button]
    fifth_answer = [By.ID, fifth_question_answer]

    sixth_button = [By.ID, sixth_question_button]
    sixth_answer = [By.ID, sixth_question_answer]

    seventh_button = [By.ID, seventh_question_button]
    seventh_answer = [By.ID, seventh_question_answer]

    eighth_button = [By.ID, eighth_question_button]
    eighth_answer = [By.ID, eighth_question_answer]

    header_button = [By.CLASS_NAME, header_button_order]
    footer_button = [By.XPATH, footer_button_order]


    @allure.step('Открываем браузер Chrome')
    def __init__(self, driver, f_locator, s_locator):
        self.driver = driver
        self.f_locator = f_locator
        self.s_locator = s_locator

    @allure.step('Нажимаем на вопрос')
    def click_on_question(self):
        self.driver.find_element(*self.f_locator).click()

    @allure.step('Смотрим на текст ответа')
    def answer_on_question(self):
        return self.driver.find_element(*self.s_locator).text

    @allure.step('Ожидаем загрузки ответа')
    def wait_for_load_answer(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.s_locator))

    @allure.step('Скроллим страницу вниз')
    def scroll_footter(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step('Нажимаем на верхнюю кнопку Заказать')
    def click_on_header_button(self):
        self.driver.find_element(*self.header_button).click()

    @allure.step('Нажимаем на нижнюю кнопку Заказать')
    def click_on_footer_button(self):
        self.driver.find_element(*self.footer_button).click()
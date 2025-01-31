from selenium import webdriver
from pages.main_page import MainPageScooter
from urls import main_page_url
import pytest

class TestQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @pytest.mark.parametrize(
        'f_locator,s_locator,text',  # Параметры соответствуют , локатору вопроса, локатору ответа и тексту для проверки с ответом на вопрос
        [
            [MainPageScooter.first_button, MainPageScooter.first_answer, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."],

            [MainPageScooter.second_button, MainPageScooter.second_answer, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."],
            [MainPageScooter.third_button, MainPageScooter.third_answer, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."],
            [MainPageScooter.fourth_button, MainPageScooter.fourth_answer, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."],
            [MainPageScooter.fifth_button, MainPageScooter.fifth_answer, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."],
            [MainPageScooter.sixth_button, MainPageScooter.sixth_answer, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."],
            [MainPageScooter.seventh_button, MainPageScooter.seventh_answer, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."],
            [MainPageScooter.eighth_button, MainPageScooter.eighth_answer, "Да, обязательно. Всем самокатов! И Москве, и Московской области."]

        ]
    )
    def test_question(self, f_locator, s_locator, text):
        self.driver.get(main_page_url)

        question = MainPageScooter(self.driver, f_locator, s_locator)
        question.check_answer_on_question()
        assert question.answer_on_question() == text



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
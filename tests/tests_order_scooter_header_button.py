from selenium import webdriver
from pages.order_page import OrderPageScooter
from urls import *
import pytest


class TestScooterOrdersHeader:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @pytest.mark.parametrize(
        'name,surname,city,sub_station,number,day_date,color,comment',
        [
            ["Денис","Иванов","Питербург","Комсомольская","89213353913","31","grey","Привет, как дела?"],
            ["Петя","Стаханов","Москва","Сокольник","89216656324","5","black","Звонить по указанному телефону"]
        ]
    )
    def test_scooter_order_header_button_check_popup_order(self, name,surname,city,sub_station,number,day_date,color,comment):
        self.driver.get(main_page_url)

        order = OrderPageScooter(self.driver)
        order.click_on_header_button()
        order.create_order(name,surname,city,sub_station,number,day_date,color,comment)
        text = "Хотите оформить заказ?\n "
        assert order.order_popup_text() == text

    def test_scooter_order_header_button_check_scooter_logo(self):
        self.driver.get(main_page_url)
        name, surname, city, sub_station, number, day_date, color, comment = "Денис","Иванов","Питербург","Комсомольская","89213353913","31","grey","Привет, как дела?"

        order = OrderPageScooter(self.driver)
        order.click_on_header_button()
        order.create_order(name,surname,city,sub_station,number,day_date,color,comment)
        order.order_popup_close()
        order.click_scooter_logo()
        assert self.driver.current_url == main_page_url

    def test_scooter_order_header_button_check_yandex_logo(self):
        self.driver.get(main_page_url)
        name, surname, city, sub_station, number, day_date, color, comment = "Денис", "Иванов", "Питербург", "Комсомольская", "89213353913", "31", "grey", "Привет, как дела?"

        order = OrderPageScooter(self.driver)
        order.click_on_header_button()
        order.create_order(name,surname,city,sub_station,number,day_date,color,comment)
        order.order_popup_close()
        order.click_yandex_logo()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert self.driver.current_url == yandex_page_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import *
from pages.base_page import BasePageScooter
import allure
class OrderPageScooter(BasePageScooter):

    name = [By.XPATH, field_name_form]
    surname = [By.XPATH, field_surname_form]
    address = [By.XPATH, field_address_form]
    subway = [By.XPATH, field_subway_form]
    subway_list = [By.CLASS_NAME, field_subway_list_form]
    phone = [By.XPATH, field_phone_form]

    next = [By.XPATH, next_button_form]

    date = [By.XPATH, field_calendar_form]
    time = [By.XPATH, field_time_form]
    day = [By.XPATH, field_time_day_form]
    color_grey = [By.ID, field_color_form_grey]
    color_black = [By.ID, field_color_form_black]
    commentary = [By.XPATH, field_comment_form]

    popup = [By.XPATH, order_popup]
    popup_close = [By.XPATH, order_popup_close]
    scooter_logo = [By.XPATH, order_scooter_logo]
    yandex_logo = [By.XPATH, order_yandex_logo]

    @allure.step('Открываем браузер Chrome')
    def __init__(self, driver):
        self.driver = driver


    @allure.step('Заполняем поле Имя')
    def set_name(self, name):
        self.driver.find_element(*self.name).send_keys(name)

    @allure.step('Заполняем поле Фамилия')
    def set_surname(self, surname):
        self.driver.find_element(*self.surname).send_keys(surname)

    @allure.step('Заполняем поле Адрес')
    def set_address(self, city):
        self.driver.find_element(*self.address).send_keys(city)

    @allure.step('Заполняем поле Метро')
    def click_on_subway_field(self, sub_station):
        self.driver.find_element(*self.subway).send_keys(sub_station)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.subway_list))
        self.driver.find_element(*self.subway_list).click()

    @allure.step('Заполняем поле Телефон')
    def set_phone(self, number):
        self.driver.find_element(*self.phone).send_keys(number)

    @allure.step('Нажимаем кнопку Далее')
    def click_next_button(self):
        self.driver.find_element(*self.next).click()

    @allure.step('Выбираем дату в календаре')
    def set_date(self, day):
        self.driver.find_element(*self.date).send_keys(day)

    @allure.step('Выбираем удобное время')
    def set_time(self):
        self.driver.find_element(*self.time).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.day))
        self.driver.find_element(*self.day).click()

    @allure.step('Выбираем цвет')
    def set_color(self, color):
        if color == "grey":
            self.driver.find_element(*self.color_grey).click()
        elif color == "black":
            self.driver.find_element(*self.color_black).click()
        else:
            self.driver.find_element(*self.color_grey).click()

    @allure.step('Пишем комментарий')
    def set_commentary(self, comment):
        self.driver.find_element(*self.commentary).send_keys(comment)

    @allure.step('Проверяем текст попапа')
    def order_popup_text(self):
        return self.driver.find_element(*self.popup).text

    @allure.step('Закрываем попап')
    def order_popup_close(self):
        self.driver.find_element(*self.popup_close).click()

    @allure.step('Нажимаем на лого Самоката')
    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

    @allure.step('Нажимаем на лого Яндекс')
    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    def click_on_footer_button_with_scroll(self):
        self.scroll_footter()
        self.click_on_footer_button()

    def create_order(self, name,surname,city, sub_station, number, day_date, color ,comment):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(city)
        self.click_on_subway_field(sub_station)
        self.set_phone(number)
        self.click_next_button()
        self.set_date(day_date)
        self.set_color(color)
        self.set_commentary(comment)
        self.set_time()
        self.click_next_button()

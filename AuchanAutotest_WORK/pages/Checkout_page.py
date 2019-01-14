#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from Locators.Locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from pages.Main_page import *


class CheckoutPage():
    """Страница чекаута"""


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 120)


    def use_delivery_to_home(self):
        """Выбор доставки на дом"""

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, Locators.delivery_to_home_tab_xpath)))
        self.driver.find_element_by_xpath(Locators.delivery_to_home_tab_xpath).click()
        return self


    def use_delivery_to_shop(self):
        """Выбор доставки в магазин"""

        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.delivery_to_shop_tab_xpath)))
        self.driver.find_element_by_xpath(Locators.delivery_to_shop_tab_xpath).click()
        return self


    def address_selection(self):
        """Клик по чекбоксу адреса"""

        self.driver.find_element_by_css_selector(Locators.address_checkbox).click()
        return self


    def store_selection(self, store_name):
        """Выбор магазина по названию"""

        list = self.driver.find_elements_by_xpath(Locators.shop_xpath)
        for item in list:
            if item.get_attribute("textContent") == store_name:
                item.click()
                break

    def store_selection_first_in_list(self):

        """Выбор магазина по счету"""
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.shop_xpath)))
        self.driver.find_element_by_xpath(Locators.shop_xpath).click()


    def use_express_delivery_checkbox(self):
        """Использовать экспресс доставку"""

        self.driver.find_element_by_xpath(Locators.express_delivery_checkbox_xpath).click()
        time.sleep(1)
        return self


    def to_2th_checkout_level(self):
        """Переход на второй шаг чекаута"""

        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.to_2th_level_checkout_button_xpath))).click()
        return self


    def text_aria_send_keys(self):
        """Ввод комментария"""

        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.text_area_xpath))).send_keys("Atalan autotest")
        time.sleep(2)
        return self


    def pay(self):
        """Вбор оплаты"""

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators.confirm_pay_button_xpath)))
        self.driver.find_element_by_xpath(Locators.confirm_pay_button_xpath).click()
        return self


    def payment_on_receipt_find_text(self, paymont_method_text):
        """Выбор оплаты по тексту"""

        #Ожидание варианта доставки "Оплата при получении" и клик, если она есть. Если нет - исключение
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//div[contains(text(), "' + paymont_method_text + '")]'))).click()
        time.sleep(3)
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, Locators.confirm_pay_button_xpath)))
        self.driver.find_element_by_xpath(Locators.confirm_pay_button_xpath).click()
        time.sleep(3)
        return self


    def use_promocode(self, promo_code):
        """Использовать промокод"""

        self.driver.find_element_by_css_selector("label[for='promocodeIhave']").click()
        self.driver.find_element_by_css_selector("div[class='field field-input-group'] input").send_keys(promo_code)
        self.driver.find_element_by_css_selector("div[class='field field-input-group'] button").click()


    def open_online_payment(self):
        """Открытие страницы онлайн оплаты"""

        self.driver.get('https://www.auchan.ru')
        main_window = self.driver.current_window_handle
        print(main_window.title)
        new_window = self.driver.get('https://www.auchan.ru/pokupki/paymentonline/index/index')
        time.sleep(5)


    def add_address(self, street, house ):
        """Добвление адреса"""

        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="add-link js-checkout__delivery-add-address"]')))
        self.driver.find_element_by_css_selector('a[class="add-link js-checkout__delivery-add-address"]').click()
        self.wait.until(EC.presence_of_element_located((By.ID, 'street'))).send_keys(street)
        self.wait.until(EC.presence_of_element_located((By.ID, 'house'))).send_keys(house)
        time.sleep(2)
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[value="Сохранить и выбрать"]'))).click()


    def put_customer_information(self, lastname, phone_num):
        """Добавление информации и пользователе"""

        if self.wait.until(EC.presence_of_element_located((By.NAME, 'lastname'))).get_attribute('value') == '':
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_widget_block"]//ul/li[2]/div[2]/a'))).click()
            self.wait.until(EC.presence_of_element_located(
                    (By.NAME, 'lastname'))).send_keys(lastname) #Ввести фамилию
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="checkout_widget_block"]//ul/li[2]/div[2]/div/a'))).click() #сохранить фамилию
            time.sleep(3)
        else:
            pass

        if self.wait.until(EC.presence_of_element_located((By.NAME, 'tel'))).get_attribute('value') == '':
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="checkout_widget_block"]//ul/li[3]/div[2]/a'))).click() #Ввести номер телефона
            self.wait.until(EC.presence_of_element_located((By.NAME, 'tel'))).send_keys(phone_num)
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH,
                                '//*[@id="checkout_widget_block"]//ul/li[3]/div[2]/div/a'))).click() # сохранить номер телефона
            time.sleep(3)
        else:
            pass



















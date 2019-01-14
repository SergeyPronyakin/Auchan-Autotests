#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from Locators.Locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time
from EmailSetting.EmailSetting import *

class ProductPage():
    """Страница продукта"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)


    def wait_loader(self):
        """Ожидание закрытия лоадера"""

        try:
            time.sleep(3)
            self.driver.find_element_by_css_selector(Locators.loader)
            self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, Locators.loader))) #ожидание завершения работы лоадера
            time.sleep(1)
            print('Дождался закрытия лоадера')
        except:
            print('Лоадера не было или успел отработать за 3 сек')

    def close_insider_frame2(self):
        """Закрытие всплывающей рекламы"""

        try:
            #Если реклама есть, закроываю ее
            self.driver.switch_to.frame(self.driver.find_element_by_class_name('sp-fancybox-iframe'))
            self.driver.find_element_by_css_selector("i[class='fa fa-times element-close-button']").click()
            self.driver.switch_to.default_content()
            time.sleep(2)
        except:
            pass


    def add_to_cart(self):
        """Добавление твоара в корзину"""

        self.driver.find_element_by_xpath(Locators.add_to_cart_button_xpath).click()
        return self


    def enter_in_product_check_stock_and_add_to_cart(self):
        """Переход в карточку товара, проверка стока и добавление в корзину"""

        """Функция перехода в карточку товара, проверка на доступность для заказа (сток) и добавление товара в корзину"""

        len_product_list = len(self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, Locators.product_item_list))))
        x=0
        while x == 0:
            self.driver.find_elements_by_css_selector(Locators.product_item_list)[
                random.randint(0, len_product_list-1)].click()
            try:
                try_to_add = 0 #Три попытки добавить товар в корзину
                while try_to_add != 3 and self.driver.find_element_by_xpath(Locators.self_delivery_blok_xpath): # если блок Самовывоз доступен только со склада
                    self.close_insider_frame2()
                    self.driver.back()
                    self.driver.find_elements_by_css_selector(Locators.product_item_list)[
                        random.randint(0, len_product_list-1)].click()
                    try_to_add += 1

                result_test_for_mail.append(
                    EmailSetting.result_test_fail("Было обнаружено " + str(try_to_add) +
                                            " товара сподряд для доставки только на склад."
                                          + "<br></br>" + "Оформление заказа остановлено.", 'FAIL'))
            except:
                self.close_insider_frame2()
                self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.add_to_cart_button_xpath))).click()
                #self.driver.find_element_by_xpath(Locators.add_to_cart_button_xpath).click()
                self.wait_loader()
                if int(self.driver.find_element_by_css_selector('i em[data-bind="text: itemsQty"]').get_attribute(
                        'textContent')) < 1:
                    self.driver.back()
                    #self.driver.back()
                    self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, Locators.product_item_list)))
                    self.driver.find_elements_by_css_selector(Locators.product_item_list)[
                        random.randint(0, len_product_list-1)].click()
                    self.close_insider_frame2()
                    self.driver.find_element_by_xpath(Locators.add_to_cart_button_xpath).click()
                time.sleep(2)
            x+=1



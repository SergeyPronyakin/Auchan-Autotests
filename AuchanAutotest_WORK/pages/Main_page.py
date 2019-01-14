#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Locators.Locators import *
from pages.Catalog_page import CatalogPage
from EmailSetting.EmailSetting import *
from Settings.Confige import *
import time
import requests


class MainPage():
    """Главная страница"""

    def __init__(self, driver, site):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        self.catalog_page = CatalogPage(self.driver)


    def open(self):
        """Открытие главной страницы"""

        self.driver.get(prod)
        return self


    def city_current_get_text(self):
        """Получение текста текущего города"""

        return self.driver.find_element_by_xpath(Locators.city_current_xpath).get_attribute('outerText')


    def city_current_click(self):
        """Клик по текущему городу"""

        self.driver.find_element_by_xpath(Locators.city_current_xpath).click()
        return self


    def city_in_list_click(self):
        """Клик по городу из списка"""

        self.driver.find_element_by_xpath(Locators.city_list_xpath).click()
        return self


    def city_in_list_get_text(self):
        """Получение текста города в таблице городов"""

        return self.driver.find_element_by_xpath(Locators.city_list_xpath).get_attribute('outerText')


    def city_search(self, city):
        """Поиск города"""

        self.driver.find_element_by_xpath(Locators.city_search_xpath).click()
        self.driver.find_element_by_xpath(Locators.city_search_xpath).send_keys(city)
        return self


    def city_found_name_click(self):
        """Поиск города по имени"""

        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.city_search_list_element_xpath)))
        self.city_found = self.driver.find_element_by_xpath(Locators.city_search_list_element_xpath)
        ActionChains(self.driver).move_to_element(self.city_found).click().perform()
        return self


    def go_to_cart_from_widget_and_check_kopeyka(self):
        """Переход в корзину через виджет с проверкой цен на комейки"""

        try:
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(Locators.cart_xpath)).perform()
            self.check_kopeyka(Locators.price_total_in_v_cart, location="Виджет корзины, итоговая цена продукта")
            self.check_kopeyka(Locators.price_total_in_v_cart, location="Виджет корзины, цена продукта")
            self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 "#header_cart_widget_block > div > section.cart-popup-section > div:nth-child(2) > div > div > footer > button")))
            get_screensots(self.driver)
            self.driver.find_element_by_css_selector(
                "#header_cart_widget_block > div > section.cart-popup-section > div:nth-child(2) > div > div > footer > button").click()
        except:
            self.driver.refresh()
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(Locators.cart_xpath)).perform()
            self.check_kopeyka(Locators.price_total_in_v_cart, location="Виджет корзины, итоговая цена продукта")
            self.check_kopeyka(Locators.price_total_in_v_cart, location="Виджет корзины, цена продукта")
            get_screensots(self.driver)
            self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 "#header_cart_widget_block > div > section.cart-popup-section > div:nth-child(2) > div > div > footer > button")))
            self.driver.find_element_by_css_selector(
                "#header_cart_widget_block > div > section.cart-popup-section > div:nth-child(2) > div > div > footer > button").click()


    def go_to_cart_from_widget(self):
        """Переход в корзину через виджет корзины"""

        try:
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(Locators.cart_xpath)).perform()
            self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 "#header_cart_widget_block > div > section.cart-popup-section > div:nth-child(2) > div > div > footer > button")))
            self.driver.find_element_by_css_selector(
                "#header_cart_widget_block > div > section.cart-popup-section > div:nth-child(2) > div > div > footer > button").click()
        except:
            self.driver.refresh()
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(Locators.cart_xpath)).perform()
            self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 "#header_cart_widget_block > div > section.cart-popup-section > div:nth-child(2) > div > div > footer > button")))
            self.driver.find_element_by_css_selector(
                "#header_cart_widget_block > div > section.cart-popup-section > div:nth-child(2) > div > div > footer > button").click()


    def main_menu_find_element_by_text(self, element_menu_name):
        """Выбор категории первого уровня по имени"""

        list = self.driver.find_elements_by_xpath(Locators.main_menu_element_xpath)
        for item in list:
            if item.get_attribute("textContent") == element_menu_name:
                item.click()
                break


    def main_menu_elements_click(self):
        """Метод проверки на пустой каталог"""

        x = 0
        y = 0
        for menu_elenent in self.driver.find_elements_by_xpath(Locators.main_menu_element_xpath):
            if self.driver.find_elements_by_xpath(Locators.main_menu_element_xpath)[x].get_attribute('textContent') == "Идеи подарков":
                break
            self.driver.find_elements_by_xpath(Locators.main_menu_element_xpath)[x].click()

            try:
                self.catalog_page.close_insider_frame2()
                self.catalog_page.catalog2_level_click()
                print(self.driver.current_url)
                if len(self.catalog_page.product_item_list_len())<1:
                    print("Не найдено товаров в категории: ", self.driver.current_url)
                    result_test_for_mail.append(EmailSetting.result_test_fail('Пусто: '+ str(self.driver.current_url),' FAIL'))
                    y+=1
            except:
                try:
                    self.catalog_page.catalog2_level_click()
                    print(self.driver.current_url)
                    if self.catalog_page.product_item_list_len()<1:
                        print("Не найдено товаров в категории: ", self.driver.current_url)
                        result_test_for_mail.append(EmailSetting.result_test_fail('Пусто: '+ str(self.driver.current_url),' FAIL'))
                        y+=1
                except:
                    if self.catalog_page.product_item_list_len()<1:
                        print("Не найдено товаров в категории: ", self.driver.current_url)
                        result_test_for_mail.append(EmailSetting.result_test_fail('Пусто: '+ str(self.driver.current_url),' FAIL'))
                        y+=1
            x+=1
            self.driver.get(preprod)
            time.sleep(2)
        if y == 0:
            result_test_for_mail.append(EmailSetting.result_test_ok('Проверка на пустые категории', 'OK'))


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


    def check_kopeyka(self, locator,location=""):
        """Проверка цен на копейки"""

        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,locator)))
            price_list = self.driver.find_elements_by_css_selector(locator)
            for price in price_list[:1]:
                if ',' in price.get_attribute("textContent"):
                    print(location, price.get_attribute("textContent"), "TEST OK")
                else:
                    print(location, price.get_attribute("textContent"), " Test FAIL")
                    self.driver.get_screenshot_as_file(
                        "/home/sergey/AuchanAutotest_WORK/screenshots/" + str(file_name_error()))
                    result_test_for_mail.append(EmailSetting.result_test_fail(str(location) + " Нет копеек", 'FAIL'))
        except:
            result_test_for_mail.append(
                EmailSetting.result_test_fail("Ошибка в функции проверки копеек - MainPage.check_kopeyka()",'FAIL'))


    def open_online_pyment_page_and_check_kopeyka(self):
        """Проверка копеек на странице онлайн оплаты"""

        self.driver.execute_script('''window.open
                    ("https://www.auchan.ru/pokupki/paymentonline/index/index","_blank");''')
        self.driver.switch_to.window(self.driver.window_handles[1])  # переключаемся в окно онлайн оплаты
        self.check_kopeyka(Locators.order_price, location='Онлайн оплата. Сумма заказа')
        self.check_kopeyka(Locators.delivery_price, location='Онлайн оплата. Сумма доставки')
        self.check_kopeyka(Locators.grand_total_price, location='Онлайн оплата. Сумма итого')
        self.driver.switch_to.window(self.driver.window_handles[0])


    def check_kopeyka_in_product_of_day_in_menu(self):
        """Проверка копеек на товаре дня"""

        self.driver.get('https://www.auchan.ru')
        self.driver.maximize_window()
        menu_list = self.driver.find_elements_by_xpath(Locators.main_menu_list_xpath)
        ActionChains(self.driver).move_to_element(menu_list[0]).perform()
        try:
            price = self.driver.find_element_by_css_selector('div.products__item-current-price.current-price > span.price-val')
            #Функция check_kopeyka() не подошла, т.к не вызывает исключения в случае ошибки (из-за того, что поиск элементов
            #осуществляется find_emementS, а не find_element. Ниже переработнная функция check_kopeyka)
            if ',' in price.get_attribute("textContent"):
                print('Цена товара дня в меню на главной', price.get_attribute("textContent"), "TEST OK")
            else:
                print('Цена товара дня в меню на главной', price.get_attribute("textContent"), " Test FAIL")
                self.driver.get_screenshot_as_file(
                    "D:\Atalan\screen\\" + str(file_name_error()))  # '/home/sergey/AuchanAutotest_WORK/screenshots/'
                result_test_for_mail.append(EmailSetting.result_test_fail(str('Цена товара дня в меню на главной') + " Нет копеек", 'FAIL'))
        except:
            print('В меню нет товара дня')
            result_test_for_mail.append(
                         EmailSetting.result_test_fail('Товар дня в меню на главной не отображается', 'FAIL'))

            """Может пригодиться. Итерация по кажлому пункту меню. Оказалась не нужна, т.к. после ховера на первый 
            пункт меню, товар дня становися видимым, в каком бы пунте меню он не был."""


    def get_footer_links(self):
        """Получение ссылко в футере сайта"""

        footer_link_list = []
        self.driver.get('https://www.auchan.ru/')
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, Locators.footer_links)))
        for link in self.driver.find_elements_by_css_selector(Locators.footer_links):
            footer_link_list.append(link.get_attribute('href'))
        return footer_link_list


    def check_status_code_footer_links(self):
        """Получение статускода по ссылкам в футере сайта"""

        for link in MainPage.get_footer_links(self):
            r = requests.get(link)
            if r.status_code != 200:
                result_test_for_mail.append(
                    EmailSetting.result_test_fail('Ответ сервера по URL в футере ' + link + " " + str(r.status_code), 'FAIL'))
            else:
                print(str(link) + " " + str(r.status_code))


    def check_OS(self):
        """Проверка на ОС"""

        if platform.system() == 'Windows':
            screenshots_dir = '/home/sergey/AuchanAutotest_WORK/screenshots/'
        else:
            screenshots_dir = 'C:\\Users\\acer-pc\PycharmProjects\AuchanAutotest_1.0\screenshots\\'
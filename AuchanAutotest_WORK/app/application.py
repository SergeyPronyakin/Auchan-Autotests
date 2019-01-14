#!/usr/bin/python
#!/path/to/venv/bin/python
# -*- coding: utf-8 -*-
from pages.Authorization_page import *
from pages.Cart_page import *
from pages.Checkout_page import *
from pages.Catalog_page import *
from checkEmail.OldUserEmail import *
from selenium import webdriver
from Customer.Customer import CustomerEmail
from EmailSetting.EmailSetting import *
from Settings.Confige import *
from AuchanOtherTests.EmailParsing import EmailParsing
from selenium.common.exceptions import UnexpectedAlertPresentException
import time
import traceback
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Application:
    """Класс набора тесткейсов"""


    def __init__(self):
        #Настройка на стороне сервера "java -jar selenium-server-standalone-3.14.0.jar"

        #self.driver = webdriver.Remote("http://127.0.0.1:14444/wd/hub", desired_capabilities={"browserName":"chrome"})
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument('disable-infobars')
        self.chrome_options.add_argument('--disable-extensions')
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        self.driver.set_page_load_timeout(120)

        #self.driver = webdriver.Chrome()

        self.authorization_page = AuthorizationPage(self.driver, prod_auth)
        self.main_page = MainPage(self.driver, prod_auth)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.catalog_page = CatalogPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.success_page = SuccessPage(self.driver)
        self.oldUserEmail = OldUserEmail()


    def windows_set_size(self, x, y):
        """Задать размеры окна"""

        print('ТЕСТ: Установка размера окна')
        self.driver.set_window_size(x, y)
        time.sleep(5)
        return self

    def driver_close(self):
        self.driver.close()

    def quit(self):
        """Закрытие драйвера"""

        print('Закрытые браузера')
        self.driver.quit()


    def split_array(self, array):
        """Редактирует элемент списка результатов"""
        return array.replace("['", '').replace("']", '').replace("', '", '')


    def send_final_mail(self):
        """Отправляет письмо, если хотя бы 1 тест fail. Если все ок, то письмо приходит с переодичностью,
         указанной в переменной mail_count с момента последнего проваленного теста"""
        path = '/home/sergey/AuchanAutotest_WORK/TextFiles/EmailCount'
        file = open(path, 'r')
        x = file.read()
        mail_count = 33 #число итераций, по достижению которого придет письмо о тестах ОК

        if len(result_test_for_mail) > 0:#если был хотя бы один тест fail, то список будет больше нуля и отправлятся
                                          #письмо с результатами
            EmailSetting.send_mail(
            EmailSetting.mail_creat(str(Application.split_array(self, str(result_test_for_mail))))) # Отправка письма
            x = 1 #Обнуляем счетчик, чтобы отсчет шел заново (с момента последнего теста fail)
            file = open(path, 'w')
            file.write(str(x))
        elif int(x) < mail_count and len(result_test_for_mail) == 0:
            #Если ошибок не было и кол-во итераций не превышено, добавляем 1 к счетчику
            x = int(x)
            x+=1
            file = open(path, 'w') #/home/sergey/AuchanAutotest_WORK/TextFiles/EmailCount'
            file.write(str(x))
        #Как только счетчик достигает заданного значения и не было ошибок, отправится письмо, что за последние mail_count все тесты
        #завершены успешно. Это нужно, чтобы понимать, что тесты вообще ходят.
        elif int(x) >= mail_count and len(result_test_for_mail) == 0:
            EmailSetting.send_mail("За последние " + str(int(mail_count/3)) + " ч. все тесты завершены успешно.")
            file = open(path, 'w')
            x = 1
            file.write(str(x))
        file.close()


    def authorization_customer(self):
        """Авторизация"""
        try:
            self.authorization_page.open(prod_auth)
            self.catalog_page.close_insider_frame2()
            self.authorization_page.click_authorization_tab()
            self.authorization_page.input_mail()
            self.authorization_page.input_password()
            self.authorization_page.submit_button()
            self.authorization_page.logout()
            #result_test_for_mail.append(EmailSetting.result_test_ok('Авторизация', 'OK'))
        except Exception as err:
            get_screensots(self.driver)
            result_test_for_mail.append(EmailSetting.result_test_fail('Авторизация' + ' ' + get_traceback(traceback, err), 'FAIL'))


    def authorization_customer_not_logout(self):
        """Авторизация без логаута"""

        print('ТЕСТ: авторизация')
        try:
            self.authorization_page.open(prod_auth)
            self.catalog_page.close_insider_frame2()
            self.authorization_page.click_authorization_tab()
            self.authorization_page.input_mail()
            self.authorization_page.input_password()
            self.authorization_page.submit_button()
            self.authorization_page.logo_click() #Переход на главную
        except Exception as err:
            get_screensots(self.driver)
            result_test_for_mail.append(EmailSetting.result_test_fail('Авторизация' + ' ' + get_traceback(traceback, err), 'FAIL'))


    def check_subscribe(self):
        """Проверка подписки на странице авторизации"""

        print('ТЕСТ: проверка подписки')
        try:
            self.authorization_page.open(prod_auth)
            self.authorization_page.input_subscribe_mail()
            self.authorization_page.find_modal_subscribe()
        except Exception as err:
            get_screensots(self.driver)
            result_test_for_mail.append(EmailSetting.result_test_fail('Подписка в футере (нет модального окна)' + ' ' + get_traceback(traceback, err), 'FAIL'))


    def wrong_pass(self):
        """Проверка на ввод неверного пароля"""

        print('ТЕСТ: сообщение о неверном пароле')
        try:
            self.authorization_page.open(prod_auth)
            self.catalog_page.close_insider_frame2()
            self.authorization_page.check_message_about_wrong_pass('23123123123')
            #result_test_for_mail.append(EmailSetting.result_test_ok('Сообщение о неверном пароле', 'OK'))
        except Exception as err:
            get_screensots(self.driver)
            result_test_for_mail.append(EmailSetting.result_test_fail('Сообщение о неверном пароле' + ' ' + get_traceback(traceback, err), 'FAIL'))


    def send_forgot_password(self):
        """Отправка нового пароля"""

        print('ТЕСТ: отправка пароля на почту')
        try:
            self.authorization_page.send_forgot_password()
            #result_test_for_mail.append(EmailSetting.result_test_ok('Восстановление пароля', 'OK'))
        except Exception as err:
            get_screensots(self.driver)
            result_test_for_mail.append(EmailSetting.result_test_fail('Восстановление пароля: ' + ' ' + get_traceback(traceback, err), 'FAIL'))


    def registration(self):
        """Регистрация"""

        print('ТЕСТ: регистрация')
        try:
            self.driver.get(prod_auth)
            time.sleep(5)
            self.catalog_page.close_insider_frame2()
            self.authorization_page.click_registration_tab()
            self.authorization_page.input_fname()
            self.chek_mail = self.authorization_page.input_mail_registration(CustomerEmail.customer_mail())
            self.authorization_page.input_password_registration()
            self.authorization_page.input_confirm_password()
            self.authorization_page.submit_registration()
            assert self.chek_mail == self.authorization_page.mail_after_registration()
            #result_test_for_mail.append(EmailSetting.result_test_ok('Регистрация', 'OK'))
        except Exception as err:
            get_screensots(self.driver)
            result_test_for_mail.append(EmailSetting.result_test_fail('Регистрация' + ' ' + get_traceback(traceback, err), 'FAIL'))


    def chek_city(self):
        """Смена города"""

        print('ТЕСТ: смена города ')
        try:
            self.driver.get(prod)
            self.catalog_page.close_insider_frame2()
            self.authorization_page.wait.until(EC.presence_of_element_located((By.XPATH, Locators.city_current_xpath)))
            self.main_page.city_current_click()
            self.city_name_in_list = self.main_page.city_in_list_get_text()
            self.main_page.city_in_list_click()
            self.authorization_page.wait.until(EC.presence_of_element_located((By.XPATH, Locators.city_current_xpath)))
            assert self.main_page.city_current_get_text() == self.city_name_in_list
            #result_test_for_mail.append(EmailSetting.result_test_ok('Смена города', 'OK'))
        except Exception as err:
            get_screensots(self.driver)
            result_test_for_mail.append(EmailSetting.result_test_fail('Смена города' + ' ' + get_traceback(traceback, err), 'FAIL'))


    def check_city_search(self):
        """Поиск города"""

        print('ТЕСТ: поиск города')
        try:
            self.city_name = 'Воронеж'
            self.catalog_page.close_insider_frame2()
            self.main_page.city_current_click()
            self.city_search_name = self.main_page.city_search(self.city_name)
            self.main_page.city_found_name_click()
            self.authorization_page.wait.until(EC.presence_of_element_located((By.XPATH, Locators.city_current_xpath)))
            assert self.city_name == self.main_page.city_current_get_text()
            #result_test_for_mail.append(EmailSetting.result_test_ok('Поиск и выбор города', 'OK'))
        except Exception as err:
            get_screensots(self.driver)
            result_test_for_mail.append(EmailSetting.result_test_fail('Поиск и выбор города' + ' ' + get_traceback(traceback, err), 'FAIL'))


    def check_express_deliveri_timeslots(self):
        """Скриншот таймслотов"""

        try:
            self.driver.get(prod + "/pokupki/customer/account/create/")
            self.catalog_page.close_insider_frame2()
            self.authorization_page.click_authorization_tab()
            self.authorization_page.input_mail()
            self.authorization_page.input_password()
            self.authorization_page.submit_button()
            self.authorization_page.logo_click()
            self.driver.maximize_window()
            self.main_page.go_to_cart_from_widget()
            self.main_page.wait_loader()
            self.cart_page.button_continue_click()
            self.main_page.wait_loader()
            self.authorization_page.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.delivery_to_home_tab_xpath)))
            self.checkout_page.use_delivery_to_home()
            self.checkout_page.use_express_delivery_checkbox()
            get_screensots(self.driver)
        except:
            get_screensots(self.driver)


    def delivery_to_home_old_customer_and_check_kopeyka(self):
        """Заказ на дом зарегистрированным пользователем с функцией проверки копеек в цене"""
        #try:

        self.catalog_page.close_insider_frame2()
        self.authorization_page.logo_click()
        self.driver.maximize_window()
        self.main_page.check_kopeyka(Locators.price_rr, location="Цена в блоке RR.")
        self.main_page.main_menu_find_element_by_text('Красота и здоровье') #выбор элемента меню по названию
        #self.driver.find_elements_by_xpath(Locators.main_menu_list_xpath)[9].click() #выбор элемента меню по счету
        self.catalog_page.catalog2_level_click()
        self.main_page.check_kopeyka(Locators.price_mainpage, location="Каталог второго уровня.")

        self.catalog_page.close_insider_frame2()
        self.product_page.enter_in_product_check_stock_and_add_to_cart() #Включает в себя проверку копеек в виджете
        self.main_page.check_kopeyka(Locators.price_product_cart, location="Карточка товара.")
        self.main_page.check_kopeyka(Locators.price_close_vidget, location="Цена закрытого виджета корзины.")
        self.main_page.go_to_cart_from_widget_and_check_kopeyka()
        self.main_page.wait_loader()
        time.sleep(2)
        self.main_page.check_kopeyka(Locators.price_product_in_cart, location="Корзина, цена продукта.")
        self.main_page.check_kopeyka(Locators.price_total_in_cart, location="Корзина, общая сумма.")
        self.cart_page.button_continue_click()
        self.main_page.wait_loader()
        self.authorization_page.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.delivery_to_home_tab_xpath)))
        self.checkout_page.use_delivery_to_home() #Выбор доставки курьером
        self.checkout_page.address_selection() #клик по первому чекбоксу с адресом
        self.main_page.check_kopeyka(Locators.price_on_checkout, location="Цена на первом шаге чекаута.")
        self.checkout_page.to_2th_checkout_level()
        self.authorization_page.wait.until(EC.presence_of_element_located((By.XPATH, Locators.text_area_xpath)))
        self.checkout_page.text_aria_send_keys()
        self.main_page.check_kopeyka(Locators.price_on_checkout, location="Цена на втором шаге чекаута.")
        self.main_page.open_online_pyment_page_and_check_kopeyka()
        #self.checkout_page.payment_on_receipt()
        self.checkout_page.use_promocode('qatestatalan')
        self.main_page.check_kopeyka(Locators.price_promocode, location="Цена с промокодом <Итого со скидкой>")
        self.main_page.wait_loader()
        self.checkout_page.payment_on_receipt_find_text("Оплата при получении")
        self.authorization_page.wait.until(EC.presence_of_element_located((By.XPATH, Locators.confirm_pay_button_xpath)))
        self.checkout_page.pay()
        #self.success_page.check_thank_block_header('(Тестовый режим с 29.10.18)Заказ на дом')
        self.driver.get(prod)
        #self.success_page.logout_from_success_page()
        # except Exception as err:
        #     get_screensots(self.driver)
        #     result_test_for_mail.append(EmailSetting.result_test_fail('(Тестовый режим с 29.10.18)Заказ на дом' + "<br></br>" + str(err), 'FAIL'))


    def delivery_to_home_old_customer(self, category1):
        """Заказ на дом зарегистрированным пользователем"""

        print('ТЕСТ: заказ на дом старый пользователь')
        try:
            self.main_page.open()
            self.catalog_page.close_insider_frame2()
            self.main_page.main_menu_find_element_by_text(category1)  # выбор элемента меню по названию
            # self.driver.find_elements_by_xpath(Locators.main_menu_list_xpath)[9].click() #выбор элемента меню по счету
            self.catalog_page.close_insider_frame2()
            self.catalog_page.catalog2_level_click()
            self.catalog_page.close_insider_frame2()
            self.product_page.enter_in_product_check_stock_and_add_to_cart()
            self.main_page.go_to_cart_from_widget()
            self.main_page.wait_loader()
            self.cart_page.button_continue_click()
            self.main_page.wait_loader()
            self.checkout_page.use_delivery_to_home()  # Выбор доставки курьером
            self.checkout_page.address_selection()  # клик по первому чекбоксу с адресом
            self.checkout_page.to_2th_checkout_level()
            self.checkout_page.text_aria_send_keys()
            self.checkout_page.payment_on_receipt_find_text("Оплата при получении")
            self.main_page.wait_loader()
            self.success_page.check_thank_block_header() #Проверка получения номера заказа на странице саксесс
            self.driver.get(prod)
        except UnexpectedAlertPresentException:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print("Текст аллерта: " + str(alert_text))
            result_test_for_mail.append(
                EmailSetting.result_test_fail('Заказ на дом (новый пользователь)' + "<br></br>"
                                              + "Текст алерта: " + str(alert_text), 'FAIL'))
            alert.accept()
        except Exception as err:
            get_screensots(self.driver)
            result_test_for_mail.append(
                EmailSetting.result_test_fail('Заказ на дом' + "<br></br>" + 'URL: ' +
                                              str(self.driver.current_url) + ' ' + get_traceback(traceback, err), 'FAIL'))


    def delivery_to_shop_old_customer(self, category1):

        print('ТЕСТ: заказ в магазин старый пользователь')
        try:
            self.main_page.open()
            self.catalog_page.close_insider_frame2()
            self.main_page.main_menu_find_element_by_text(category1)  # выбор элемента меню по названию
            # self.driver.find_elements_by_xpath(Locators.main_menu_list_xpath)[9].click() #выбор элемента меню по счету
            self.catalog_page.close_insider_frame2()
            self.catalog_page.catalog2_level_click()
            self.catalog_page.close_insider_frame2()
            self.product_page.enter_in_product_check_stock_and_add_to_cart()
            self.main_page.go_to_cart_from_widget()
            self.main_page.wait_loader()
            self.cart_page.button_continue_click()
            self.main_page.wait_loader()
            self.checkout_page.use_delivery_to_shop()  # Выбор доставки в магазин
            self.main_page.wait_loader()
            self.checkout_page.store_selection("Москва АТАК (501) Ключевая")  # выбор магазина из списка по имени
            self.checkout_page.to_2th_checkout_level()
            self.authorization_page.wait.until(EC.presence_of_element_located((By.XPATH, Locators.text_area_xpath)))
            self.checkout_page.text_aria_send_keys()
            self.checkout_page.payment_on_receipt_find_text("Оплата при получении")
            self.main_page.wait_loader()
            self.success_page.check_thank_block_header()
            self.driver.get(prod)
        except UnexpectedAlertPresentException:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print("Текст аллерта: " + str(alert_text))
            result_test_for_mail.append(
                EmailSetting.result_test_fail(
                    'Заказ в магазин (новый пользователь)' + "<br></br>"  + "Текст алерта: "
                    + str(alert_text),'FAIL'))
            alert.accept()
        except Exception as err:
            get_screensots(self.driver)
            result_test_for_mail.append(
                EmailSetting.result_test_fail('Заказ в магазин (новый пользователь)' + "<br></br>" + 'URL: '
                                              + str(self.driver.current_url) + ' ' + get_traceback(traceback, err),'FAIL'))


    def delivery_to_home_new_customer(self, category1):
        """Заказ на дом новый пользователь"""

        print('ТЕСТ: заказ на дом новый пользователь')
        try:
            self.main_page.open()
            self.catalog_page.close_insider_frame2()
            self.main_page.main_menu_find_element_by_text(category1)  # выбор элемента меню по названию
            # self.driver.find_elements_by_xpath(Locators.main_menu_list_xpath)[9].click() #выбор элемента меню по счету
            self.catalog_page.close_insider_frame2()
            self.catalog_page.catalog2_level_click()
            self.catalog_page.close_insider_frame2()
            self.product_page.enter_in_product_check_stock_and_add_to_cart()
            self.main_page.go_to_cart_from_widget()
            self.main_page.wait_loader()
            self.cart_page.button_continue_click()
            self.main_page.wait_loader()
            self.checkout_page.use_delivery_to_home()  # Выбор доставки курьером
            self.main_page.wait_loader()
            self.checkout_page.add_address('Новодмитровская','2')
            self.main_page.wait_loader()
            self.checkout_page.put_customer_information('Фамилия','9000010000')
            self.checkout_page.to_2th_checkout_level()
            self.checkout_page.text_aria_send_keys()
            self.checkout_page.payment_on_receipt_find_text("Оплата при получении")
            self.success_page.check_thank_block_header()  # Проверка получения номера заказа на странице саксесс
            self.driver.get(prod)
        except UnexpectedAlertPresentException:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print("Текст аллерта: " + str(alert_text))
            result_test_for_mail.append(
                EmailSetting.result_test_fail(
                    'Заказ на дом(новый пользователь)' + "<br></br>"
                    + "Текст алерта: " + str(alert_text), 'FAIL'))
            alert.accept()
        except Exception as err:
            get_screensots(self.driver)
            result_test_for_mail.append(
                EmailSetting.result_test_fail('Заказ на дом (новый пользователь)' +
                                        "<br></br>" + 'URL: ' + str(self.driver.current_url) + ' ' + get_traceback(traceback, err), 'FAIL'))


    def delivery_to_shop_new_customer(self, category1):
        """Заказ в магазин новый пользователь"""

        print('ТЕСТ: заказ в магазин новый пользователь')

        try:
            self.main_page.open()
            self.catalog_page.close_insider_frame2()
            self.main_page.main_menu_find_element_by_text(category1)  # выбор элемента меню по названию
            # self.driver.find_elements_by_xpath(Locators.main_menu_list_xpath)[10].click()
            self.catalog_page.close_insider_frame2()
            self.catalog_page.catalog2_level_click()
            self.catalog_page.close_insider_frame2()
            self.product_page.enter_in_product_check_stock_and_add_to_cart()
            self.main_page.go_to_cart_from_widget()
            self.main_page.wait_loader()
            self.cart_page.button_continue_click()
            self.main_page.wait_loader()
            self.checkout_page.use_delivery_to_shop()  # Выбор доставки в магазин
            self.checkout_page.store_selection("Москва АТАК (501) Ключевая")  # выбор магазина из списка по имени
            self.main_page.wait_loader()
            self.checkout_page.put_customer_information('ФамилияМагазин', '9000010000')
            self.checkout_page.to_2th_checkout_level()
            self.checkout_page.text_aria_send_keys()
            self.checkout_page.payment_on_receipt_find_text("Оплата при получении")
            self.success_page.check_thank_block_header()
            self.driver.get(prod)
        except UnexpectedAlertPresentException:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print("Текст аллерта: " + str(alert_text))
            result_test_for_mail.append(
                EmailSetting.result_test_fail(
                    'Заказ на дом(новый пользователь)' + "<br></br>" + "Текст алерта: " +
                    str(alert_text), 'FAIL'))
            alert.accept()
        except Exception as err:
            get_screensots(self.driver)
            result_test_for_mail.append(EmailSetting.result_test_fail(
                'Заказ в магазин(новый пользователь)' + "<br></br>" + 'URL: ' +
                str(self.driver.current_url) + ' ' + get_traceback(traceback, err), 'FAIL'))


    def delivery_to_shop_old_customer_region(self, category1):

        print('ТЕСТ: заказ в магазин старый пользователь, регион')
        try:
            self.main_page.open()
            self.catalog_page.close_insider_frame2()
            self.main_page.main_menu_find_element_by_text(category1)  # выбор элемента меню по названию
            # self.driver.find_elements_by_xpath(Locators.main_menu_list_xpath)[9].click() #выбор элемента меню по счету
            self.catalog_page.close_insider_frame2()
            self.catalog_page.catalog2_level_click()
            self.catalog_page.close_insider_frame2()
            self.product_page.enter_in_product_check_stock_and_add_to_cart()
            self.catalog_page.close_insider_frame2()
            self.main_page.go_to_cart_from_widget()
            self.main_page.wait_loader()
            self.cart_page.button_continue_click()
            self.main_page.wait_loader()
            self.checkout_page.use_delivery_to_shop()  # Выбор доставки в магазин
            self.main_page.wait_loader()
            self.main_page.city_current_click()
            self.main_page.city_in_list_click()
            self.checkout_page.store_selection_first_in_list()
            self.main_page.wait_loader()
            #self.checkout_page.store_selection("Москва АТАК (501) Ключевая")  # выбор магазина из списка по имени
            self.checkout_page.to_2th_checkout_level()
            self.authorization_page.wait.until(EC.presence_of_element_located((By.XPATH, Locators.text_area_xpath)))
            self.checkout_page.text_aria_send_keys()
            self.checkout_page.payment_on_receipt_find_text("Оплата при получении")
            self.main_page.wait_loader()
            self.success_page.check_thank_block_header()
            self.driver.get(prod)
        except UnexpectedAlertPresentException:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print("Текст аллерта: " + str(alert_text))
            result_test_for_mail.append(
                EmailSetting.result_test_fail(
                    'Заказ в магазин (старый пользователь) регион' + "<br></br>" + "Текст алерта: "
                    + str(alert_text),'FAIL'))
            alert.accept()
        except Exception as err:
            get_screensots(self.driver)
            result_test_for_mail.append(
                EmailSetting.result_test_fail('Заказ в магазин (старый пользователь) регион' + "<br></br>" + 'URL: '
                                              + str(self.driver.current_url) + ' ' + get_traceback(traceback, err), "FAIL"))


    def check_email_price(self):
        """Проверка цены в письме"""

        print('ТЕСТ: проверка цены в письме')
        EmailParsing.CheckEmailPrice.get_first_text_block(EmailParsing.CheckEmailPrice.get_email_massage())


    def check_footer_links(self):
        """Проверка ссылок футера сайта на статускод"""

        print('ТЕСТ: проверка ссылок футера')
        try:
            self.main_page.get_footer_links()
            self.main_page.check_status_code_footer_links()
        except:
            get_screensots(self.driver)
            result_test_for_mail.append(
                EmailSetting.result_test_fail('Проверка ссылок в футере сайта', 'FAIL'))


    def podbor_shin(self):
        """Проверка подборщика шин"""

        self.catalog_page.podbor_shin()


    def remove_files(self):
        """Удаление файлов из папки со скриншотами"""
        dir = str(screenshots_path_linux)
        for screenshot_name in os.listdir(dir):
            full_dir = str(dir) + str(screenshot_name)
            os.remove(full_dir)


    def logging(self):
        """Логирование"""

        file = open('/home/sergey/AuchanAutotest_WORK/log.txt', 'w')
        for entry in self.driver.get_log('browser'):
            file.write("Сообщение:" + str(entry) + '\n')
        file.close()



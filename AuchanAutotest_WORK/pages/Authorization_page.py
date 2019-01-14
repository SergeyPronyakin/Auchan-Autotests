#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Locators.Locators import *
from Settings.Confige import *
from Customer.Customer import *
from selenium.webdriver.common.action_chains import ActionChains
import time

class AuthorizationPage():
    """Страница авторизации и регистрании пользователя https://www.auchan.ru/pokupki/customer/account/create/"""


    def __init__(self, driver, site):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)


    def open(self,site):
        """Открытие страницы"""

        self.driver.get(site)
        return self


    def click_authorization_tab(self):
        """Клик по вкладке авотризации"""

        self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/section[2]/div/section/header/div[1]'))).click()
        #self.driver.find_element_by_xpath('/html/body/div[1]/div/section[2]/div/section/header/div[1]').click()
        return self


    def click_registration_tab(self):
        """Клик по вкладке регистрации"""

        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.registration_tab_xpath))).click()
        #self.driver.find_element_by_xpath(Locators.registration_tab_xpath).click()
        return self


    def input_mail(self):
        """Ввод почты"""

        self.driver.find_element_by_id(Locators.login_email_id).send_keys(email_customer)
        return self


    def input_password(self):
        """Ввод пароля"""

        self.driver.find_element_by_id(Locators.login_password_id).send_keys(password_customer)
        return self


    def submit_button(self):
        """Клик по кнопке Отправить"""
        self.driver.find_element_by_css_selector(Locators.submit_button).click()
        return self


    def input_mail_registration(self, customer_mail):
        """Ввод новой почты для регистрации"""

        self.driver.find_element_by_id(Locators.email_registration_id).send_keys(customer_mail)
        return self


    def input_fname(self):
        """Ввод имени"""

        self.driver.find_element_by_id(Locators.first_name_id).send_keys('QA.autotest')
        return self


    def input_password_registration(self):
        """Ввод пароля для регистрации"""

        self.driver.find_element_by_id(Locators.password_id).send_keys('12345670')
        return self


    def input_confirm_password(self):
        """Ввод подтверждения пароля"""

        self.driver.find_element_by_id(Locators.password_confirmation_id).send_keys('12345670')
        return self


    def click_checkbox_agry(self):
        """Установка чекбокса в форме регистрации"""

        self.driver.find_element_by_xpath(Locators.agry_checkbox_xpath).click()
        return self


    def submit_registration(self):
        """Отправка формы регистрации"""

        self.driver.find_element_by_xpath(Locators.registration_button_xpath).click()
        return self


    def mail_after_registration(self):
        """Получение текста почты на странице ЛК"""

        self.driver.find_element_by_xpath(Locators.mail_after_registration_xpath).get_attribute("outerText")
        return self


    def logout(self):
        """Лоагут"""

        self.driver.find_element_by_xpath(Locators.log_out_xpath).click()
        return self


    def check_mail_customer_in_account_page(self):
        """Проверка почты на странице ЛК"""

        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, Locators.mail_in_account)))
        return self.driver.find_element_by_css_selector(Locators.mail_in_account).get_attribute('textContent')


    def check_message_about_wrong_pass(self, wrong_password):
        """Функция отправки неверного пароля и проверки вывода сообщения"""

        self.driver.find_element_by_id(Locators.login_email_id).send_keys(email_customer)
        self.driver.find_element_by_id(Locators.login_password_id).send_keys(wrong_password)
        self.driver.find_element_by_css_selector(Locators.submit_button).click()
        time.sleep(2)
        return self.driver.find_element_by_css_selector(Locators.wrong_password_message).get_attribute('textContent')


    def send_forgot_password(self):
        """Отправка забытого пароля"""

        self.driver.find_element_by_css_selector(Locators.forgot_password_link).click()
        self.driver.find_element_by_name(Locators.mail_input_wrong_password_name).send_keys("atalan.autotest@mail.ru")
        self.driver.find_element_by_xpath(Locators.submit_button_forgot_password_xpath).click()
        self.wait.until(EC.presence_of_element_located((By.ID, Locators.modal_window_send_password_id)))


    def logo_click(self):
        """Клик по логотипу"""

        self.driver.find_element_by_css_selector(Locators.logo).click()
        return self


    def input_subscribe_mail(self):
        """Ввод почты для подписки"""

        sub_mail=CustomerEmail.customer_mail()
        self.driver.find_element_by_name(Locators.subscribe_input_name).send_keys(sub_mail)
        self.driver.find_element_by_id(Locators.subscribe_btn_id).click()
        return self


    def find_modal_subscribe(self):
        """Поиск окна после подписки"""

        self.wait.until(EC.presence_of_element_located((By.ID, Locators.subscribe_modal_id)))
        overlay = self.wait.until(EC.presence_of_element_located((By.ID, Locators.modal_subsbribe_overlay_id)))
        ac = ActionChains(self.driver)
        ac.move_to_element(overlay).move_by_offset(100, 100).click().perform()
        return self


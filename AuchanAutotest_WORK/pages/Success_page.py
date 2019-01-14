#!/usr/bin/python
# -*- coding: utf-8 -*-

from pages.Product_page import ProductPage
from Locators.Locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from EmailSetting.EmailSetting import *
from Settings.Confige import result_test_for_mail, file_name_error
import time
from selenium.webdriver.support.wait import WebDriverWait


class SuccessPage(ProductPage):


    def check_thank_block_header(self):
        """Проверка номера заказа на странцие саксесс"""
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.order_id_xpath)))


    def logout(self):
        """Лоагут"""

        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.logout_link_xpath))).click()
        except Exception as err:
            self.driver.get_screenshot_as_file(
                str(screenshots_path_linux) + str(file_name_error()))
            result_test_for_mail.append(
                EmailSetting.result_test_fail('Success page не получена/получена некорректно' + "<br></br>" + str(err), 'FAIL'))


    def get_order(self):
        """Получение текста номера заказа"""

        self.odrer_number = self.driver.find_element_by_xpath(Locators.order_id_xpath).get_attribute('textContent')
        return self.odrer_number


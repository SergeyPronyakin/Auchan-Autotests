#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Locators.Locators import *
import time
from EmailSetting.EmailSetting import *


class CatalogPage():
    """Страница каталога"""


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)


    def close_insider_frame2(self):
        """Закрытие всплывающего окна рекламы"""

        time.sleep(10)
        try:
            #Если реклама есть, закроываю ее
            self.driver.switch_to.frame(self.driver.find_element_by_class_name('sp-fancybox-iframe'))
            self.driver.find_element_by_css_selector("i[class='fa fa-times element-close-button']").click()
            self.driver.switch_to.default_content()
            time.sleep(2)
        except:
            pass


    def catalog2_level_click(self):
        """Клик по категории второго уровня"""

        #Первый элемент
        #self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="category__item-title"] a'))).click()
        #Второй элемент
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[class="category__item-title"] a')))
        self.driver.find_elements_by_css_selector('div[class="category__item-title"] a')[2].click()


    def product_item_list_len(self):
        """Кол-во товаров на странице каталога"""

        self.len_items = self.driver.find_elements_by_css_selector(Locators.product_item_list)
        return len(self.len_items)


    def podbor_shin(self):
        """Проверка наличия столбцов и элементов в подборщике"""

        def split_array(array):
            """Редактирует элемент списка результатов"""
            return array.replace("['", '').replace("']", '').replace("', '", '')
        try:
            self.driver.get('https://www.auchan.ru/podbor-shin')
            self.close_insider_frame2()
            self.driver.find_elements_by_xpath('//*[@id="crw"]/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div')[0].click()
            time.sleep(2)
            self.driver.find_elements_by_xpath('//*[@id="crw"]/div[1]/div[2]/div[2]/div[1]//div[2]/div')[1].click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="crw"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[1]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="crw"]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[2]/div[1]').click()
            time.sleep(2)

        except Exception as err:
            self.driver.get_screenshot_as_file(
                str(screenshots_path_linux_PROP) + str(file_name_error()))
            result_test_for_mail_PROP.append(EmailSetting.result_test_fail('Подборщик работает' + "<br></br>" + str(err), 'FAIL'))
            EmailSetting.send_mail_PROP(EmailSetting.mail_creat(str(split_array(str(result_test_for_mail_PROP)))))

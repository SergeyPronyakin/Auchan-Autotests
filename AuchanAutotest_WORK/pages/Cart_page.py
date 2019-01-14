#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Locators.Locators import *
import time


class CartPage():
    """Страница корзины"""


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)


    def button_continue_click(self):
        """Клик по кнопке Оформить в корзине"""

        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.button_continue_xpath))).click()
        return self



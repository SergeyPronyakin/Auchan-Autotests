#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Запуск набора тестов"""

from pages.Catalog_page import CatalogPage
from EmailSetting.EmailSetting import *
import requests



def check_status_code(URL):
    def split_array(array):
        """Редактирует элемент списка результатов"""
        return array.replace("['", '').replace("']", '').replace("', '", '')
    r = requests.get(URL)
    if r.status_code !=200:
        result_test_for_mail.append(EmailSetting.result_test_fail("Ответ страницы " + str(URL) + " " +  "<" + str(r.status_code) + ">", 'FAIL'))
        EmailSetting.send_mail_without_screen(EmailSetting.mail_creat(str(split_array(str(result_test_for_mail)))))
        return False
    else:
        print("Тест ОК. Статус код = " + str(r.status_code))
        return True


if __name__ == '__main__':
    check_status_code('https://www.auchan.ru/')


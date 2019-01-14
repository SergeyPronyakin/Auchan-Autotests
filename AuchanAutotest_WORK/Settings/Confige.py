#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
import platform
import traceback
"""Настройки"""

prod = 'http://www.auchan.ru'
prod_auth = 'http://www.auchan.ru/pokupki/customer/account/create/'
preprod = 'https://auchan4.atalan.net'
preprod_auth = 'https://auchan4.atalan.net/pokupki/customer/account/create/'


email_customer = "spronyakin2017@yandex.ru"
password_customer = "12345670"
result_test_for_mail = []
result_test_for_mail_PROP = []

screenshots_path_linux =  '/home/sergey/AuchanAutotest_WORK/screenshots/' #'/home/supertester/AutotestsAuchan/screenshots/' #
screenshots_path_linux_PROP = '/home/supertester/AutotestsAuchan/screenshotsPROP/'

screenshots_path_windows = 'C:\\Users\\acer-pc\PycharmProjects\AutotestsAuchan\screenshots\\'
screenshots_path_windows_PROP = 'C:\\Users\\acer-pc\PycharmProjects\AutotestsAuchan\\screenshotsPROP\\'


def file_name_error():
    """Имя файла скриншота"""

    now = datetime.now()
    file_error_name = 'Screenshot_' + str(now)[5:-7].replace(' ', '_').replace(':','') + '.png'
    return file_error_name


def get_screensots(driver):
    """Функция получения скриншота"""

    if platform.system() == 'Windows':
        driver.get_screenshot_as_file(
            str(screenshots_path_windows) + str(file_name_error()))
    else:
        driver.get_screenshot_as_file(
            str(screenshots_path_linux) + str(file_name_error()))


def get_traceback(traceback,err):
    """Вывод ошибки"""

    traceback = str(''.join(traceback.format_exception(etype=type(err), value=err, tb=err.__traceback__)))
    return traceback.replace('\n', "<br></br>")


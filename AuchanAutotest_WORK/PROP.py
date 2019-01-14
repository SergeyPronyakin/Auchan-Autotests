#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Запуск набора тестов"""

from app.application import *
from EmailSetting.EmailSetting import *

def main():
    app = Application()
    app.podbor_shin()
    #app.send_final_mail()
    #EmailSetting.send_mail_PROP(EmailSetting.mail_creat(str(app.split_array(str(result_test_for_mail)))))  #Отправка писем
    app.quit()


if __name__ == '__main__':
    main()

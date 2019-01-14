#!/usr/bin/python
# -*- coding: utf-8 -*-

from imaplib import IMAP4_SSL
from pages.Success_page import *
import time

class OldUserEmail():

    def check_email_old_user(self, order):
        time.sleep(120)


        HOST = "imap.yandex.ru"
        PORT = 993
        USER = "USER"
        PASSWORD = "PASSWORD"

        connection = IMAP4_SSL(host=HOST, port=PORT)
        connection.login(user=USER, password=PASSWORD)
        status, msgs = connection.select('inbox')
        assert status == 'OK'

        data = connection.search(None, "ALL")
        ids = data[1][0]
        ids_list = ids.split()
        ids_list.reverse()

        search_mail_list = []
        for mail in ids_list[0:20]:
            email_data = connection.fetch(mail, "RFC822")

            x=1
            if  str(order) not in str(email_data):
                print(str(order), 'fail')
                x+=1
            else:
                result_test_for_mail.append(
                    EmailSetting.result_test_ok('Письмо по заказу ' + order + " получено", 'ОК'))
                search_mail_list.append('yes')
                print('OK')

            if x==20:
                result_test_for_mail.append(
                    EmailSetting.result_test_fail('Письмо по заказу ' + order + " не получено за X сек", 'FAIL'))

        if len(search_mail_list)>1:
            print('Письмо задвоилось')
            print(search_mail_list)
            result_test_for_mail.append(
            EmailSetting.result_test_fail('Письмо по заказу '+ order + " задвоилось" , 'FAIL'))


        connection.close()
        connection.logout()

oldUserEmail = OldUserEmail()

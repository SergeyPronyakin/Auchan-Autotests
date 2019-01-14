#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Запуск набора тестов"""

from app.application import *
from EmailSetting.EmailSetting import *
from Settings.Confige import *
from datetime import datetime
from AuchanBack.AuchanRequests import *
import logging


class SecondaryTests:


    def main(self):
        app = Application()

        start = datetime.now()
        print("Tests start " + str(start)[:-7])

        if auchanRequests.check_status_code_for_start('https://www.auchan.ru') == True:
            app.windows_set_size(1080, 1080)         #Устанока размера окна
            app.wrong_pass()                         #Сообщение о неверном пароле
            app.send_forgot_password()               #Восстановление пароля
            app.chek_city()                          #Смена города
            app.check_city_search()                  #Поиск города
            app.check_footer_links()                 #Проверка ответа сервера по ссылкам в футере
            app.quit()                               #Закрытие драйвера
            #app.send_final_mail()                    #Отправка письма с отчетом
        else:
            print('Сайт лежит! Отослал письмо!')

        end = datetime.now()
        print("Tests completed " + str(end)[:-7])

secondaryTests = SecondaryTests()
if __name__ == '__main__':
    secondaryTests.main()



#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Запуск набора тестов"""

from app.application import *
from EmailSetting.EmailSetting import *
from Settings.Confige import *
from datetime import datetime
from AuchanBack.AuchanRequests import *

class HomeDeliveryOldCustomer:


    def main(self):
        app = Application()

        start = datetime.now()
        print("Tests start " + str(start)[:-7])

        if auchanRequests.check_status_code_for_start('https://www.auchan.ru') == True:
            app.windows_set_size(1800, 1080)         #Устанока размера окна
            app.authorization_customer_not_logout()
            app.delivery_to_home_old_customer('Красота и здоровье')      #Заказ с доставкой на дом
            app.quit()                               #Закрытие драйвера
            #app.send_final_mail()                    #Отправка письма с отчетом
        else:
            print('Сайт лежит! Отослал письмо!')

        end = datetime.now()
        print("Tests completed " + str(end)[:-7])


homeDeliveryOldCustomer = HomeDeliveryOldCustomer()
if __name__ == '__main__':
    homeDeliveryOldCustomer.main()



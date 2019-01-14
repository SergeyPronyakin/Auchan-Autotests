#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Запуск набора тестов"""

from app.application import *
from EmailSetting.EmailSetting import *
from Settings.Confige import *
from datetime import datetime
from AuchanBack.AuchanRequests import *

class DeliveryToShopOldCustomerRegion:

    def main(self):
        app = Application()

        start = datetime.now()
        print("Tests start " + str(start)[:-7])

        if auchanRequests.check_status_code_for_start('https://www.auchan.ru') == True:
            app.windows_set_size(1800, 1080)         #Устанока размера окна
            app.authorization_customer_not_logout()  #Авторизация без разлогирования
            app.delivery_to_shop_old_customer_region('Красота и здоровье')      #Заказ с доставкой в магазин
            app.quit()                               #Закрытие драйвера
            #app.send_final_mail()                    #Отправка письма с отчетом
        else:
            print('Сайт лежит! Отослал письмо!')

        end = datetime.now()
        print("Tests completed " + str(end)[:-7])


deliveryToShopOldCustomerRegion = DeliveryToShopOldCustomerRegion()
if __name__ == '__main__':
    deliveryToShopOldCustomerRegion.main()



#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Запуск набора тестов"""

from app.application import *
from AuchanBack.AuchanRequests import *


class HomeDeliveryNewCustomer:


    def main(self):
        app = Application()

        start = datetime.now()
        print("Tests start " + str(start)[:-7])

        if auchanRequests.check_status_code_for_start('https://www.auchan.ru') == True:
            app.windows_set_size(1800, 1080)         #Устанока размера окна
            app.registration()                       # Регистрация
            app.delivery_to_home_new_customer('Красота и здоровье')      #Заказ с доставкой на дом новый пользователь
            app.quit()                               #Закрытие драйвера
            #app.send_final_mail()                    #Отправка письма с отчетом
        else:
            print('Сайт лежит! Отослал письмо!')

        end = datetime.now()
        print("Tests completed " + str(end)[:-7])


homeDeliveryNewCustomer = HomeDeliveryNewCustomer()
if __name__ == '__main__':
    homeDeliveryNewCustomer.main()



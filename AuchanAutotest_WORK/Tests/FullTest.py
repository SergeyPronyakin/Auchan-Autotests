#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Запуск набора тестов"""

from app.application import *
from EmailSetting.EmailSetting import *
from Settings.Confige import *
from datetime import datetime
from AuchanBack.AuchanRequests import *


class AllTests:

    def main(self):
        app = Application()

        start = datetime.now()
        print("Tests start " + str(start)[:-7])

        if auchanRequests.check_status_code_for_start('https://www.auchan.ru') == True:
            app.windows_set_size(1800, 1080)         #Устанока размера окна
            app.wrong_pass()                         #Сообщение о неверном пароле
            app.send_forgot_password()               #Восстановление пароля
            app.authorization_customer_not_logout()  #Авторизация без разлогирования
            app.delivery_to_home_old_customer('Красота и здоровье')      #Заказ с доставкой на дом
            app.delivery_to_shop_old_customer('Бытовая техника')      #Заказ с доставкой в магазин
            app.success_page.logout()                #Вызвать при необходимости разлогироваться
            app.registration()                       #Регистрация
            app.delivery_to_home_new_customer('Зоотовары')      #Заказ с доставкой на дом новый пользователь
            app.delivery_to_shop_new_customer('Красота и здоровье')      #Заказ с доставкой в магазин новый пользователь
            app.chek_city()                          #Смена города
            app.check_city_search()                  #Поиск города
            app.check_footer_links()                 #Проверка ответа сервера по ссылкам в футере
            app.quit()                               #Закрытие драйвера
            app.send_final_mail()                    #Отправка письма с отчетом

        else:
            print('Сайт лежит! Отослал письмо!')

        end = datetime.now()
        print("Tests completed " + str(end)[:-7])


allTests = AllTests()
if __name__ == '__main__':
    allTests.main()



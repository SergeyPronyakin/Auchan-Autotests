from Tests.DeliveryToHomeNewCustomer import *
from Tests.DeliveryToHomeOldCustomer import *
from Tests.DeliveryToShopNewCustomer import *
from Tests.DeliveryToShopOldCustomer import *
from Tests.SecondaryTests import *
from Tests.DeliveryToShopOldCustomerRegion import *
from app.application import *
from EmailSetting.EmailSetting import *



def main():

    """Запуск сценариев атомарно"""

    try:
        homeDeliveryNewCustomer.main()
        time.sleep(1)
    except Exception as err:
        EmailSetting.send_mail_without_screen('Упс... тест доставки на дом нового пользователя не запущен по ошибке webdriver: ' + "<br></br>" + str(err))

    try:
        homeDeliveryOldCustomer.main()
        time.sleep(1)
    except Exception as err:
        EmailSetting.send_mail_without_screen('Упс... тест доставки на дом старого пользователя не запущен по ошибке webdriver: ' + "<br></br>" + str(err))

    try:
        deliveryToShopOldCustomer.main()
        time.sleep(1)
    except Exception as err:
        EmailSetting.send_mail_without_screen('Упс... тест доставки в магазин старого пользователя не запущен по ошибке webdriver: ' + "<br></br>" + str(err))

    try:
        deliveryToShopNewCustomer.main()
        time.sleep(1)
    except Exception as err:
        EmailSetting.send_mail_without_screen('Упс... тест доставки в магазин нового пользователя не запущен по ошибке webdriver: ' + "<br></br>" + str(err))

    try:
        deliveryToShopOldCustomerRegion.main()
        time.sleep(1)
    except Exception as err:
        EmailSetting.send_mail_without_screen('Упс... тест второстепенных тестов не запущен по ошибке webdriver: ' + "<br></br>" + str(err))

    try:
        secondaryTests.main()
        time.sleep(1)
    except Exception as err:
        EmailSetting.send_mail_without_screen('Упс... тест доставки в магазин старого пользователя в регион не запущен по ошибке webdriver: ' + "<br></br>" + str(err))


    application.send_final_mail()
    application.quit()


if __name__ == '__main__':
    main()


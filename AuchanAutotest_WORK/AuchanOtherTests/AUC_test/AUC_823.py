from datetime import timedelta, datetime
import re

dif_time = 3 #блокировка IP адреса в минутах
registration_message = "С вашего IP-адреса была замечена подозрительная активность. " \
                       "В связи с этим, просим Вас зарегистрироваться на сайте " \
                       "в 18:42. Все товары, собранные в корзину на сайте, не пропадут. Спасибо, что Вы с нами!"

time_in_massage = re.findall('(\d+)', registration_message) #выделяем время из сообщения
now = datetime.now()

#Приводим значение времени к типу "datetime"
current_time = datetime.strftime(datetime.now(),"%H:%M")
message = ":".join(time_in_massage)
message_time = datetime.strptime(message,"%H:%M" )
registration_time = datetime.strptime(current_time,"%H:%M" )

#Проверка времени сообщения
if message_time <= registration_time:
    #Если время в сообщении прошедшее либо равно времени регистрации (текущему)
    print("TEST FAIL. Отправляю сообщение на почту")
    print("Делаю скрин")
    print('Внимание! Время сообщения некорректное!' + '\n' +
          "Время регистрации:" + str(registration_time)[10:-3] + "\n" +
          "Время, указанное в сообщении:" + str(message_time)[10:-3])
elif message_time > registration_time:
    #Если время сообщения больше, чем время регистрации
    registration_next_time = registration_time + timedelta(minutes=dif_time)
    if registration_next_time == message_time:
        #Если время возможной регистрации совмадает с временем в сообщении (Тест ОК)
        print('Время сообщения указано корректно')
        print("TEST ОК. Отправляю сообщение на почту")
    else:
        #Если время сообщения больше, но не равно времени следующей возможной регистрации
        print("TEST FAIL. Отправляю сообщение на почту")
        print("Делаю скрин")
        print("Дата следующей возможной регистрации" + str(registration_time)[10:-3]+ "\n" +
        "не соответсвует времени, указанном в сообщении" + str(message_time)[10:-3])


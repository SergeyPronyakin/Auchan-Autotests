import email.message
import re
import imaplib
import  quopri
from Settings.Confige import result_test_for_mail
from EmailSetting.EmailSetting import *
class CheckEmailPrice():

    def get_email_massage(self):
        """Функция получения тела письма"""

        mail = imaplib.IMAP4_SSL('imap.yandex.ru')
        login = mail.login('spronyakin2017@yandex.ru', "CobrA69")
        mail.list()
        mail.select("inbox")

        result, data = mail.search(None, "ALL")
        ids = data[0] # Получаем сроку номеров писем
        id_list = ids.split() # Разделяем ID писем
        latest_email_id = id_list[-1] # Берем последний ID
        result, data = mail.fetch(latest_email_id, "(RFC822)") # Получаем тело письма (RFC822) для данного ID
        raw_email = data[0][1].decode()

        email_message = email.message_from_string(raw_email)
        return email_message

    def get_first_text_block(self, email_message_instance):
        """Функция парсинга и проверки цен письма"""

        maintype = email_message_instance.get_content_maintype()
        if maintype == 'multipart':
            for part in email_message_instance.get_payload():
                if part.get_content_maintype() == 'text':
                    print(email_message_instance.get_payload())
                    return part.get_payload()
        elif maintype == 'text':
            msg = quopri.decodestring(email_message_instance.get_payload()).decode('utf-8') #Тело сообщения
            #Вывод html тела сообщения
            #print("************************")
            #msg = email_message_instance.get_payload()
            #print(msg)
            #print("************************")


            """Парсинг цены"""
            try:
                from BeautifulSoup import BeautifulSoup
            except ImportError:
                from bs4 import BeautifulSoup
            html =  msg
            parsed_html = BeautifulSoup(html, "lxml")
            cost_span = parsed_html.body.find_all('span')
            cost_div = parsed_html.body.find_all('div')


            #ТЕСТОВЫЕ СПИСКИ СОДЕРЖИМОГО ТЕГОВ
            # cost_span = ['\nВ течение 2-4 дней                            ', 'Atalan autotest', 'Артикул:', '343026', '\n6105            р.\n', 'р.', '\n61,05р.', 'р.', 'р.', 'р.', '\n110.10                            р.\n', 'р.']
            # cost_div = ['\r\n\t\t\t\t\t\t\tЧекаут Новый, Ваш заказ принят.\r\n\t\t\t\t\t\t', '\r\n\t\t\t\t\t\t\tБлагодарим за покупку!\r\n\t\t\t\t\t\t', '\n\nЧекаут Новый                                    ', '\n\n+7(233)423-34-32                                    ', '\n\nОплата при получении                            ', '\n\nВ магазин                            ', '\n\nВ течение 2-4 дней                            ', '\nAtalan autotest', '\n\nМосква АТАК (501) Ключевая                                                            ', '\nЕжедневно с 09:00 до 22:00', '\n\n\nКлючевая д.16/29                                                                \n', '\n61.05                            р.', '\n49.00 р.', '\nСпасибо, что выбрали нас!', '\nБесплатная линия службы поддержки', '\n8 (800) 700-5-800']


            """Парсинг тега span"""
            cost_span_list = []
            for i in cost_span:
                cost_span_list.append(i.text) #!!!!!  .text
            print(cost_span_list)
            all_price_list = []
            for i in cost_span_list:
               #a = re.findall('^[0-9]*[.,]?[0-9]+$', i) #целые и дробные числа с точкой и запчятой
               a = re.findall('[0-9]+[.,][0-9]{2}', i) #!только дробные числа с точкой и запчятой (целые игнорирует) и двумя цифрами после точки или запятой
               all_price_list.append(a)
            print(all_price_list)


            """Парсинг тега div"""
            cost_div_list = []
            for i in cost_div:
                cost_div_list.append(i.text) #!!!!!! .text
            print(cost_div_list)
            new_list = []
            for i in cost_div_list:
                # a = re.findall('^[0-9]*[.,]?[0-9]+$', i) #целые и дробные числа с точкой и запчятой
                a = re.findall('[0-9]+[.,][0-9]{2}',i)  # !только дробные числа с точкой и запчятой (целые игнорирует) и двумя цифрами после точки или запятой
                all_price_list.append(a)
            print(all_price_list)


            """Проверка наличия цен с копейками"""
            floatPrice_list = []
            for i in all_price_list:
                if i != []:
                    floatPrice_list.append(i)


            count_float_price = 5
            if len(floatPrice_list) < count_float_price:
                result_test_for_mail.append(EmailSetting.result_test_fail("Цены с копейками в транзакционном письме. Необходимый минимум - " + str(count_float_price) + "<br></br>"
                                                                          + "Фактически - " + str(len(floatPrice_list)), 'FAIL'))
            # else:
            #     result_test_for_mail.append(EmailSetting.result_test_ok('Копейки в транзакционном письме', 'OK'))


CheckEmailPrice = CheckEmailPrice()






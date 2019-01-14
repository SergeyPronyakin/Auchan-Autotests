#!/usr/bin/python
# -*- coding: utf-8 -*-

from email.header import Header
from datetime import datetime
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import io
from email import encoders
from smtplib import SMTP_SSL
import os
from Settings.Confige import *
import mimetypes                                          # Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
from email import encoders                                # Импортируем энкодер
from email.mime.base import MIMEBase                      # Общий тип
from email.mime.text import MIMEText                      # Текст/HTML
from email.mime.image import MIMEImage                    # Изображения
from email.mime.audio import MIMEAudio
import platform
import time


"""Настройки почты"""
username = 'spkobra@mail.ru'
mail_sender = 'spkobra@mail.ru'
mail_receiver = 'spkobra2@gmail.com', 'olechka56741@gmail.com', 'ashnayder@atalan.net', 'asidorenko@atalan.net', 'dsavinov@atalan.net', 'ekozlov@atalan.net'#, 'ecommerce_it@auchan.ru' , 'ashnayder@atalan.net', 'asidorenko@atalan.net'
mail_receiver_to_spkobra2gmailcom = 'spkobra2@gmail.com'
mail_receiver_PROP = 'spkobra2@gmail.com', 'artem@atalan.net'
mail_sender_login = 'spkobra@mail.ru'
mail_sender_password = 'CobrAPronyA032986'
mail_server = "smtp.mail.ru"
subject = u'Автотест Auchan' #Тема письма
subject_PROP = u'Автотест подборщик' #Тема письма


class EmailSetting():
    """Генерация и отправка писем"""


    def result_test_ok(self, test, result):
        """Строка тест ОК"""

        self.result_test_for_mail = '<tr><th>' + str(datetime.strftime(datetime.now(), "%Y.%m.%d")) + '</th><th>' \
                                    + str(datetime.strftime(datetime.now(), "%H:%M")) + '</th><th>' + str(test) + \
                                    '</th>' + '<th bgcolor = "green">' + str(result) + '</th></tr>'
        return self.result_test_for_mail


    def result_test_fail(self, test, result):
        """Строка тест FAIL"""

        self.result_test_for_mail = '<tr><th>' + str(datetime.strftime(datetime.now(), "%Y.%m.%d")) + '</th><th>' \
                                    + str(datetime.strftime(datetime.now(), "%H:%M")) + '</th><th>' + str(test) + \
                                    '</th>' + '<th bgcolor = "red">' + str(result) + '</th></tr>'
        return self.result_test_for_mail


    def mail_creat(self, result_test):
        """Создание письма"""

        self.body_mail_part1 = '<!DOCTYPE HTML><html><head><meta charset="utf-8">' \
                          '<title>Таблица результатов автотестов</title>' \
                          '</head><body><table border="1"><caption>Результаты автотестов Auchan</caption>' \
                          '<tr><th>Дата</th><th>Время</th><th>Тест</th><th>Результат</th></tr>' \
                          + "\n"
        self.body_mail_part2 = '</table></body></html>'
        return self.body_mail_part1 + result_test + self.body_mail_part2



    def send_mail_without_screen(self, body):
        """Отправка письма без скриншотов"""

        server = smtplib.SMTP(mail_server)  # Используемый сервер
        msg = MIMEText(body, _charset='utf-8', _subtype='html')  # формирование тела письма, body - чтение из html файла
        msg['Subject'] = Header(subject, 'utf-8')  # формирование заголовка пиьма
        # Отпавляем письмо
        server.starttls()
        server.ehlo()
        server.login(username, mail_sender_password)
        server.sendmail(mail_sender, mail_receiver_to_spkobra2gmailcom, msg.as_string())
        server.quit()


    def send_mail(self, body):
        """Отправка письма со скриншотами"""

        server = smtplib.SMTP(mail_server)  # Используемый сервер
        multy_msg = MIMEMultipart()
        multy_msg['Subject'] = Header(subject, 'utf-8')  # формирование заголовка пиьма
        multy_msg.preamble = 'Auchan autotests'
        msg = MIMEText(body, _charset='utf-8', _subtype='html')  # формирование тела письма, body - чтение из html файла
        multy_msg.attach(msg)

        #attachment
        dir = str(screenshots_path_linux)
        for screenshot_name in os.listdir(dir):
            full_dir = str(dir) + str(screenshot_name)
            filename = os.path.basename(full_dir)

            if os.path.isfile(full_dir):  # Если файл существует
                ctype, encoding = mimetypes.guess_type(full_dir)  # Определяем тип файла на основе его расширения
                if ctype is None or encoding is not None:  # Если тип файла не определяется
                    ctype = 'application/octet-stream'  # Будем использовать общий тип
                maintype, subtype = ctype.split('/', 1)  # Получаем тип и подтип
                if maintype == 'text':
                    with open(full_dir, 'rb') as fp:
                        file = MIMEText(fp.read(), _charset='utf-8', _subtype='html')
                        fp.close()
                elif maintype == 'image':
                    with open(full_dir, 'rb') as fp:
                        file = MIMEImage(fp.read(), _subtype=subtype)
                        fp.close()
                else:  # Неизвестный тип файла
                    with open(full_dir, 'rb') as fp:
                        file = MIMEBase(maintype, subtype)  # Используем общий MIME-тип
                        file.set_payload(fp.read())  # Добавляем содержимое общего типа (полезную нагрузку)
                        fp.close()
                encoders.encode_base64(file)  # Содержимое должно кодироваться как Base64
                file.add_header('Content-Disposition', 'attachment', filename=filename) # Добавляем заголовки
                multy_msg.attach(file)  # Присоединяем скриншоты
        # Отпавляем письмо
        server.starttls()
        server.ehlo()
        server.login(username, mail_sender_password)
        server.sendmail(mail_sender, mail_receiver, multy_msg.as_string())
        server.quit()
        #Удаление скринов из папки
        for screenshot_name in os.listdir(dir):
            full_dir = str(dir) + str(screenshot_name)
            os.remove(full_dir)


    def send_mail_PROP(self, body):
        """Отправка письма проекта Подборщик """

        server = smtplib.SMTP(mail_server)  # Используемый сервер
        multy_msg = MIMEMultipart()
        multy_msg['Subject'] = Header(subject_PROP, 'utf-8')  # формирование заголовка пиьма
        multy_msg.preamble = 'Auchan autotests'
        msg = MIMEText(body, _charset='utf-8', _subtype='html')  # формирование тела письма, body - чтение из html файла
        multy_msg.attach(msg)

        #attachment
        dir = str(screenshots_path_linux_PROP)
        for screenshot_name in os.listdir(dir):
            full_dir = str(dir) + str(screenshot_name)
            filename = os.path.basename(full_dir)

            if os.path.isfile(full_dir):  # Если файл существует
                ctype, encoding = mimetypes.guess_type(full_dir)  # Определяем тип файла на основе его расширения
                if ctype is None or encoding is not None:  # Если тип файла не определяется
                    ctype = 'application/octet-stream'  # Будем использовать общий тип
                maintype, subtype = ctype.split('/', 1)  # Получаем тип и подтип
                if maintype == 'text':
                    with open(full_dir, 'rb') as fp:
                        file = MIMEText(body, _charset='utf-8', _subtype='html')
                        fp.close()
                elif maintype == 'image':
                    with open(full_dir, 'rb') as fp:
                        file = MIMEImage(fp.read(), _subtype=subtype)
                        fp.close()
                else:  # Неизвестный тип файла
                    with open(full_dir, 'rb') as fp:
                        file = MIMEBase(maintype, subtype)  # Используем общий MIME-тип
                        file.set_payload(fp.read())  # Добавляем содержимое общего типа (полезную нагрузку)
                        fp.close()
                encoders.encode_base64(file)  # Содержимое должно кодироваться как Base64
                file.add_header('Content-Disposition', 'attachment', filename=filename) # Добавляем заголовки
                multy_msg.attach(file)  # Присоединяем скриншоты
        # Отпавляем письмо
        server.starttls()
        server.ehlo()
        server.login(username, mail_sender_password)
        server.sendmail(mail_sender, mail_receiver_PROP, multy_msg.as_string())
        server.quit()
        #Удаление скринов из папки
        for screenshot_name in os.listdir(dir):
            full_dir = str(dir) + str(screenshot_name)
            os.remove(full_dir)


EmailSetting = EmailSetting()

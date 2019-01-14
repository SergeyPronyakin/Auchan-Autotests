import requests
from email.header import Header
from datetime import datetime
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def send_mail(body):

    username = 'spkobra@mail.ru'
    mail_sender = 'spkobra@mail.ru'
    mail_receiver = 'spkobra2@gmail.com'
    mail_sender_login = 'spkobra@mail.ru'
    mail_sender_password = 'CobrAPronyA032986'
    mail_server = "smtp.mail.ru"
    subject = u'Auchan FEED'  # Тема письма

    server = smtplib.SMTP(mail_server)  # Используемый сервер
    msg = MIMEText(body, _charset='utf-8', _subtype='html')  # формирование тела письма, body - чтение из html файла
    msg['Subject'] = Header(subject, 'utf-8')  # формирование заголовка пиьма
    # Отпавляем письмо
    server.starttls()
    server.ehlo()
    server.login(username, mail_sender_password)
    server.sendmail(mail_sender, mail_receiver, msg.as_string())
    server.quit()


def get_feed_statuscode(URL):
    r = requests.get(URL).text
    if 'Обратитесь позже, фид еще не сгенерирован.' in r:
        print("Фид не сгенерирован: "+ str(r))
    else:
        send_mail("Фид сгенерирован: "+ URL)

get_feed_statuscode("https://auchan4.atalan.net/pokupki/yandexmarket/index/yandexSearchFeedMobApp")
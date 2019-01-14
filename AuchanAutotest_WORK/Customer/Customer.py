#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from EmailSetting.EmailSetting import *
from Settings.Confige import *
from imaplib import IMAP4_SSL
from pages.Success_page import *

class CustomerEmail:
    """Класс почты пользователя"""

    def now_time(self):
       self.now = str(datetime.now()).replace(' ','_').replace('.','').replace(':','').replace('-','')[:-6]
       return self.now
    
    def customer_mail(self):
       self.name = str('example' + str(self.now_time()) + '@p33.org')
       return self.name


CustomerEmail = CustomerEmail()



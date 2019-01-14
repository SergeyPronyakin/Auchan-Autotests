from bs4 import BeautifulSoup
import urllib.request
from app.application import *
from EmailSetting.EmailSetting import *
import urllib
import base64
import requests
import urllib.request


application = Application()


class AuchanRequests():
    """Тестирование бэка"""


    def split_array(self, array):
        """Редактирует элемент списка результатов"""
        return array.replace("['", '').replace("']", '').replace("', '", '')


    def check_status_code_for_start(self, URL):
        """Проверка главной страницы на статускод"""

        r = requests.get(URL)
        if r.status_code != 200:
            result_test_for_mail.append(
                EmailSetting.result_test_fail("Ответ страницы " + str(URL) + " - " + str(r.status_code) + "<br></br>"
                                              + 'Тесты не будут запущены', 'FAIL'))
            EmailSetting.send_mail_without_screen(EmailSetting.mail_creat(str(auchanRequests.split_array(str(result_test_for_mail)))))
            return False
        else:
            print("Тест ОК. Статус код = " + str(r.status_code))
            return True


    def check_all_links(self, URL):

        try:
            resp = urllib.request.urlopen(URL)
            soup = BeautifulSoup(resp, 'html.parser')
            fail_status_code_list = []

            for link in soup.find_all('a', href=True):
                if 'https' in link['href'] and requests.get(link['href']).status_code != 200:
                    fail_status_code_list.append(link['href'])
                    result_test_for_mail.append(
                        EmailSetting.result_test_fail('URL ' + str(link['href']) + " ответ: " + str(requests.get(link['href']).status_code), 'FAIL'))
                    print(str(link['href']), str(requests.get(link['href']).status_code))

            if len(fail_status_code_list) > 0:
                EmailSetting.send_mail_without_screen(
                    EmailSetting.mail_creat(str(auchanRequests.split_array(str(result_test_for_mail)))))

        except:
            result_test_for_mail.append(
                EmailSetting.result_test_fail('Запуск тестов по проверке StatusCode невозможен. Попытка будет осуществлена позднее, согдасно кронлисту', 'FAIL'))
            EmailSetting.send_mail_without_screen(
                EmailSetting.mail_creat(str(auchanRequests.split_array(str(result_test_for_mail)))))



    def check_all_links2(self, URL):

        resp = urllib.request.urlopen(URL)
        soup = BeautifulSoup(resp, 'html.parser')
        x = 1
        for link in soup.find_all('a', href=True):
            if 'https' in link['href']:
                print(x, link['href'])
                x += 1



    def check_all_links_admin(self, URL):

        #try:
        s = requests.Session()
        password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        top_level_url = URL
        password_mgr.add_password(None, top_level_url, 'auchan', 'atalan321')
        handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
        opener = urllib.request.build_opener(handler)
        opener.open(URL)
        urllib.request.install_opener(opener)

        text = s.post(URL, auth=('spronyakin','qwerty1234'), cookies = s.cookies)
        print(text.text)

        resp = urllib.request.urlopen(URL)
        soup = BeautifulSoup(resp, 'html.parser')
        fail_status_code_list = []

        for link in soup.find_all('a', href=True):
            print(link)
            if 'https' in link['href'] and requests.get(link['href']).status_code != 200:
                fail_status_code_list.append(link['href'])
                result_test_for_mail.append(
                    EmailSetting.result_test_fail(
                        'URL ' + str(link['href']) + " ответ: " + str(requests.get(link['href']).status_code),
                        'FAIL'))
                print(str(link['href']), str(requests.get(link['href']).status_code))

        if len(fail_status_code_list) > 0:
            EmailSetting.send_mail_without_screen(
                EmailSetting.mail_creat(str(auchanRequests.split_array(str(result_test_for_mail)))))

       
auchanRequests = AuchanRequests()

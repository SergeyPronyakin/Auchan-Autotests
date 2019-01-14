#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Запуск набора тестов"""
from AuchanBack.AuchanRequests import *
from app.application import *


def main():
    auchanRequests.check_all_links_admin('https://preprod-auchan.atalan.net/pokupki/index.php/admin/dashboard/index/key/9f92511187ffde0ab55231d2364426c247a417cd5effb1c3950a5cd79de4e314/')

if __name__ == '__main__':
    main()




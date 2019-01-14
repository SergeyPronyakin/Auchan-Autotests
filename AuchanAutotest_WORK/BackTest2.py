#!/usr/bin/python
# -*- coding: utf-8 -*-
from AuchanBack.AuchanRequests import *


def main():
    """Проверка всех URL на сайте"""
    auchanRequests.check_all_links('https://www.auchan.ru/')


if __name__ == '__main__':
    main()




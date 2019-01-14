# -*- coding: utf-8 -*-
import xml.dom.minidom as minidom
from collections import Counter

class OfferDublicate:


    def CheckEmptyTag(self, xml_file, tag):
        """Проверка на заполненность тега"""
        xml = minidom.parse(xml_file)
        items = xml.getElementsByTagName("item")
        for item in items:
            try:
                brend = item.getElementsByTagName(tag)
                value_brend = brend[0].firstChild.nodeValue
            except:
                id = item.getElementsByTagName("g:id")
                print("В ID " + str(id[0].firstChild.nodeValue) + " не заполнен тег <g:brand>")

        print("********************************************************************************")


    def OfferDublicate(self, xml_file):
        xml = minidom.parse(xml_file)
        items = xml.getElementsByTagName("item")
        itemList = []
        for item in items:
            id = item.getElementsByTagName("g:id")
            idVaue = id[0].firstChild.nodeValue
            itemList.append(idVaue)
            itemListCountFunc = Counter(itemList)
            for i in {e: count for e, count in itemListCountFunc.items() if count > 1}:
                print('Обнаружен дубль товара! ', i)


OfferDublicate = OfferDublicate()

if __name__ == "__main__":
    OfferDublicate.CheckEmptyTag("/home/sergey/Загрузки/Ашан/Фиды/getgooglefeed_test2.xml", "g:brand")
    #OfferDublicate.OfferDublicate("/home/sergey/Загрузки/Ашан/Фиды/getgooglefeed_test2.xml")




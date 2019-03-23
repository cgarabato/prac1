# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:46:00 2019

@author: Boss
"""

import os
import requests
from bs4 import BeautifulSoup

url="https://latiendadevalentina.com/moda"
page = requests.get(url)
print(page)
bs = BeautifulSoup(page.content,features="lxml")
#bs = BeautifulSoup(html, 'html.parser')
articulos = bs.findAll('article')
resultados = []
print(len(articulos))
for art in articulos:
    print("--------------------------------")
    print("Artículo: " + art.meta["content"])
    print(art.div.img["data-full-size-image-url"])
    print(art.div.a["data-orig-href"])
    sub_page = requests.get(art.div.a["data-orig-href"])
    sub_content = BeautifulSoup(sub_page.content,features="lxml")
    price = sub_content.find("span", {"itemprop":"price"})
    print(price["content"])    
    spans = sub_content.find(id="content-wrapper")
    description = sub_content.find("div", {"class":"product-information"})
    print(description.div.p)
    
    #print("Precio " + str(spans))
    #print(secciones[3].div)
    
    ##for i in range(len(secciones)):
   ##     print("_------- ")
   ##     print(secciones[i])
    ##print(art.meta["content"] + "contiene " + str(len(secciones)))
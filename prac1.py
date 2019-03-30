# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 17:21:41 2019

@author: Boss
"""

import os
import requests
from bs4 import BeautifulSoup
import csv

class Articulo(object):
    
    def __init__(self, nombre, color, url, talla):
        self.nombre = nombre
        self.color = color
        self.url = url
        self.talla = talla
      
    def __iter__(self):
        return iter([self.nombre, self.color, self.url, self.talla])
    
    def imprimir_articulo(self):
        print ("--------------------------")
        print (" Articulo  " + self.nombre)
        print (" Color  " + self.color)        
        print (" Url  " + self.url)
        print (" Talla  " + self.talla)

url="https://latiendadevalentina.com/moda"
page = requests.get(url)
bs = BeautifulSoup(page.content,features="lxml")
articulos = bs.findAll('article')
resultados = []

listado_articulos = []

encabezado = ["nombre", "color", "url", "talla"]
listado_articulos.append(encabezado)

for art in articulos:
    nombre_articulo = art.meta["content"]
    
    #Buscamos el color
    listado_palabras = nombre_articulo.split()
    color = listado_palabras[-1]
    if (color.isupper() == False):
        color = "N/A"
    url = art.div.a["data-orig-href"]
    sub_page = requests.get(art.div.a["data-orig-href"])
    
    #Subpagina
    sub_content = BeautifulSoup(sub_page.content,features="lxml")
    price_tag = sub_content.find("span", {"itemprop":"price"})
    precio = price_tag["content"] 
    
    # Separa palabras
    lista_palabras_url = url.split("/")
    talla = lista_palabras_url[-1]
    description = sub_content.find("div", {"class":"product-information"})
    
    #Creamos el objeto
    articulo = Articulo( str(nombre_articulo), str(color) , str(url) ,str(talla))
    
    #Creamos la lista
    listado_articulos.append(articulo)

#Creamos el fichero de texto
with open("productos.csv", 'w') as csv_file:
    wr = csv.writer(csv_file, delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    for art in listado_articulos:
        wr.writerow(list(art))
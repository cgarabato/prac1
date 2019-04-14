# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 17:27:51 2019

@author: Boss
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:53:15 2019

@author: Boss
"""

import os
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import urllib
import urllib.request
import random
from urllib import parse
from urllib import robotparser

class Articulo(object):
    
    def __init__(self, categoria, subcategoria, nombre, color, url, talla,
                 precio, descripcion):
        self.categoria = categoria   
        self.subcategoria = subcategoria   
        self.nombre = nombre
        self.color = color
        self.url = url
        self.talla = talla
        self.precio = precio
        self.descripcion = descripcion        
      
    def __iter__(self):
        return iter([self.categoria, self.subcategoria, self.nombre,
                     self.color, self.url, self.talla, self.precio,
                     self.descripcion])
    
    def imprimir_articulo(self):
        print ("______________________")
        print (" Categoria  " + self.categoria) 
        print (" SubCategoria  " + self.subcategoria)       
        print (" Articulo  " + self.nombre)
        print (" Color  " + self.color)        
        print (" Url  " + self.url)
        print (" Talla  " + self.talla)
        print (" Precio  " + self.precio)
        print (" Descripcion  " + self.descripcion)
     
url="https://latiendadevalentina.com/"

user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

url="https://latiendadevalentina.com/"

#Random user agent
user_agent = random.choice(user_agent_list)
#Set la headers 
headers = {'User-Agent': user_agent}


page = requests.get(url, headers=headers)
#print(page)

soup = BeautifulSoup(page.content, 'lxml')

sections_names=[]

#Se recogen las secciones 
for wrapper in soup.find_all('a', {"class":" a-niveau1"}):
   link = wrapper.get('href')   
   link_splitted = link.split("/")
   string_section = link_splitted[-1]
   if (string_section.find("?") == -1):
       sections_names.append(string_section)

#Lista de artículos
listado_articulos = []

encabezado = ["categoria", "subcategoria", "nombre", "color",
              "url", "talla", "precio", "descripcion"]
listado_articulos.append(encabezado)

print(sections_names)

pageId = 1
for index in range(len(sections_names)): 
    
    pageId = 1
    prohibido = False
    
    if ((sections_names[index] == 'zapatos') or (sections_names[index] == 'moda')):      
       
        seccion = sections_names[index]
        while(prohibido != True):
            urlBase="https://latiendadevalentina.com/"
            page_query = "?page="+str(pageId)
            pageId += 1
            section_url = urlBase + seccion + page_query
            page = requests.get(section_url, headers=headers)
            
            ## Se agrega excepción para verificar que la página sea va
            if(page.status_code != 200):
                prohibido = True
                pass
                
            bs = BeautifulSoup(page.content,features="lxml")
            articulos = bs.findAll('article')

            ## Si ya no hay artículos que verificar se salta a la siguiente sección
            if (articulos == []):
                prohibido = True
                pass

            for art in articulos:

                h2=art.find("h2", {"class": "h3 product-title"}) 
                nombre = h2.a.text # Nombre del artículo
                nombre= nombre.strip('/')
                #Buscamos el color (solo mayus)
                listado_palabras = nombre.split()

                color = listado_palabras[-1]

                if (color.isupper() == False):
                    color = "N/A"
                else:
                    nombre =(' '.join(nombre.split()[:-1]))            
                    
                    listado2 = nombre.split()#Segundo color
                    
                    if (listado2[-1].isupper() == True):
                       color = color + "-" + listado2[-1]
                       nombre =(' '.join(nombre.split()[:-1]))
                  

                url = art.div.a["data-orig-href"]
                sub_page = requests.get(art.div.a["data-orig-href"], headers=headers)
                        
                #Buscamos la categoría
                categoria = sections_names[index]
              
                
                #Buscamos la subcategoría
                subcategoria = listado_palabras[0]
                   
                #Buscamos el precio
                precioFind=art.find("div", {"class": "product-price-and-shipping"})               
                precio= (precioFind.find("span", {"class": "price"}).text)
                                   
                #Buscamos la Subpágina
                sub_content = BeautifulSoup(sub_page.content,features="lxml")
    
                # Tallas - Separa las palabras de la url
                lista_palabras_url = url.split("/")
                talla = lista_palabras_url[-1]#Tallas iniciales
    
                #Buscamos Descripción 
                descFind = sub_content.find("div", {"class":"product-information"})
                description1 = descFind.find("div", {"itemprop":"description"})
                descripcion = description1.get_text()

                #Creamos la lista
                if (str(nombre).strip()!=""):

                    if subcategoria in nombre:
                        nombre = nombre.replace(subcategoria, "", 1)
                    
                    articulo = Articulo(str(categoria), str(subcategoria),
                                        str(nombre), str(color) , str(url) ,
                                        str(talla), str(precio), str(descripcion))

                    listado_articulos.append(articulo)          

                #Impresión del objetos articulo
                articulo.imprimir_articulo()

                sleep(3) #Control del tiempo          

#Creamos el fichero de texto csv
with open("valentinaTextil.csv", 'w') as csv_file:
    wr = csv.writer(csv_file, delimiter=',',quoting=csv.QUOTE_NONNUMERIC,lineterminator='\n')
    for art in listado_articulos:
        wr.writerow(list(art))
        

        
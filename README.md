# practica1

# PriceScraper


## Descripción
En esta práctica se aplican técnicas de web scraping mediante el lenguaje de programación Python para extraer así datos de la web y generar un dataset. En este caso se extraen los precios de diferentes productos textiles de la página web https://latiendadevalentina.com/. 

Se extraen solo los datos de las secciones de zapatos y moda, porque solo nos interesa el textil y además muchos productos se repiten en otras secciones. Los datos extraídos son:
"categoría", "subcategoría", "nombre_artículo", "color", "url", "talla", "precio", "descripción"
Enlace al repositorio:
https://github.com/cgarabato/prac1

## Miembros del equipo
La actividad ha sido realizada de manera individual por Carlos Garabatos.

### Para ejecutar el script es necesario instalar las siguientes bibliotecas:
* pip install csv
* pip install requests
* pip install urllib
* pip install beautifulsoup4
* pip install random
* pip install time

## Ficheros del código fuente
1. main.py: Contiene toda la implementación del proceso de scraping.
1. README.md: 
1. csv: Resultado de la exportación de datos.

## Desarrollo
Se han enviado un mail al gestor la tienda, solicitandole permiso para el scraping, y no se ha recibido respuesta.
Posteriormente, durante el proceso de desarrollo la web a sufrido cambios en la etiquetación de precios de las páginas de producto-detalle, las secciones de la cabecera(p.e. han suprimido la seccion homewear) y han modificado el fichero robots.txt.

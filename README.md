# Curso webscraping y Xpath

[Notas de estudiantes](https://github.com/rb-one/curso-webscrapping-con-xpath-/blob/master/Notes/notes.md)

## RESUMEN: Introducción webscraping y xpath

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Web scraping Es una técnica usada por data scientist y backend developers para extraer información de internet, accede a esto usando el protocolo de tranferencias de hipertexto (HTTP) o a través de un navegador. Los datos extraídos usualmente son guardados en una
base de datos, incluso en una hoja de cálculo para posteriores análisis. Puede hacerse de manera automática (bot) o manualmente.

Xpath es un lenguaje que sirve para apuntar a las partes de un documento XML. Xpath modela un documento XML como un árbol de nodos. Existen diferentes tipos de nodos: elementos, atributos, texto.

## RESUMEN ¿Por qué aprender web scraping hoy?

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Las agencias de seguridad, aplicaciones que comparan precios más baratos entre hoteles, apliaciones de ecommerce que comparan
precios entre diferentes competidores usan web scraping.
Las agencias de marketing para analziar el contenido de tweets que se vuelven virales. En general el web scraping es una habilidad muy valiosa
para cuando no tienes acceso a una API.

Es posible realizar web scraping con diferentes lenguajes de programación, como R o Js ( y sus respectivas librerías)
sin embargo Py es por excelencia el lenguaje de programación para esta tarea. Cuenta con la comunidad más grande para implementarlo.

## RESUMEN: Python: el lenguaje más poderoso para extraer datos

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

### Request

Es una librería nos permite controlar HTTP. El conjunto de reglas o protocolos de comunicación. En el enlace está la documentación en
español plano.

"El gobierno de su Majestad, Amazon, Google, Twilio, Mozilla, Heroku, PayPal,
NPR, Obama for America, Transifex, Native Instruments, The Washington Post, Twitter,
SoundClound, Kippt, Readability y algunas organizaciones Federales de los Estados Unidos de América utilizan Requests internamente.
Ha sido descargado más de 8,000,000 de veces desde PyPI. "

### Beautiful Soup

Es una libería de pyhton qué nos sirve para extraer información HTML y XML. Recibe este nombre debido a un poema con el mismo nombre
de Lewins Carroll en Alicia en el pais de la maravillas.

"Beautiful Soup, so rich and green,
Waiting in a hot tureen!
Who for such dainties would not stoop?
Soup of the evening, beautiful Soup! "

### Selenium

Podemos crear navegadores fantasmas para controlar sitios web de manera automática. Bots.

### Scrapy

Permite escribir reglas para extraer los datos, es extensible por diseño,
es rápido y simple. Es usado por el UK para recolectar datos de la población.

### HERRAMIENTAS DE WEBSCRAPPING

Los siguientes son soluciones que no necesitan codear, y que en su mayoría tienen un propósito específico.
Enfocados ecomerce o a funciones como tomar screenshots de PDFs. Automatizar y agendar actividades, y las soluciones están dadas
como pluggins en el navegador hasta servicios.

ParseHub
webscraper.io
LIBRERÍAS Y LENGUAJES

Rvest Es una librería inspirada en Beautiful soup, diseñada para
cosechar y recolectar datos de HTML. Se usa en R studio.

Puppeteer Es una librería de Js que puede usarse para
diferentes propósitos entre los cuales el webscrapping es uno.

### HTTP

HTTP es un protocolo de comunicación entre computadoras en internet, en el cual se tiene un cliente y un servidor

La transmicion de datos en HTTP se basa en el envio de una request y la llegada del response

Códigos de estado HTTP más comunes

Status code 200 – OK.
Status code 301 – Moved Permanently.
Status code 302 – Moved Temporarily.
Status code 403 – Forbidden
Status code 404 – Not Found
Status code 500 – Internal Server Error
Status code 503 ­– Service Unavailable

https://www.ionos.com/digitalguide/hosting/technical-matters/the-most-important-http-status-codes-at-a-glance/


RESUMEN: Fundamentos de la WEB

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

HTTP: Hypertext Transfer Protocol

Conjunto de reglas por el cual dos computadores se comunican. Un cliente y un servidor. El cliente realiza peticiones a servidores.

Una petición se ve así:

```txt
# Request
GET / HTTP/1.1
Host: developer.mozilla.org  Accept-Language: fr

# Response  HTTP/1.1 200 OK
Date: Sat, 09 Oct 2010 14:28:02 GMT
Server: Apache
Last-Modified: Tue, 01 Dec 2009 20:18:22 GMT  ETag: "51142bc1-7449-479b075b2891b"
Accept-Ranges: bytes  Content-Length: 29769  Content-Type: text/html
<!DOCTYPE html... (here comes the 29769 bytes of the  requested web page)
```

HEADERS
Permiten al cliente y el servidor passar información adicional con un request o response HTTP.
Pueden agruparse en las siguientes categorías:

Generales : Aplica para request y responses pero no tiene relación con la data transmitida en el cuerpo
Request : Contienen más información acerca del recurso a ser fetch (extraer)
Response : Contiene información adicional sobre respuestas. Como ubicación o el Server provider.
Entity : Contien información acerca del recurso del cuerpo.
Existen muchas cabeceras o headers como:

Accept
Authorization
Link
Location
Save-Data
Puedes consultar aquí toda la documentación sobre las cabeceras o Headers

HTTP nos permite transportar, HTML, CSS, webAPIs, Js.
Y se vale de protcolos como IP, TCP, UDP para comunicarse con el servidor, mediante TLS se hace la encriptación
Y el DNS asigna nombres a direcciones IP.

STATUS CODE :

Los estados son la forma en que el servidor da respuesta de las peticiones.

1.- Respuestas informativas (100–199).
2.- Respuestas satisfactorias (200–299).
3.- Redirecciones (300–399).
4.- Errores de los clientes (400–499).
5.- Errores de los servidores (500–599).

La siguiente hace parte de la documentación de Mozilla:

STATUS RESPONSE

MANEJO DE STATUS CODES

Una opción rápida para manejarlas es usar la librería Request

Shell*

1. Abre un ambiente virtual.
2. En la carpeta de trabajo: pip install request

Luego en pyhton

```python
## Una idea sobre el manejo de los status Code.

import requests

response_platzi = requests.get('https://api.platzi.com')
print(response_platzi)
# <Response [404]>

if response_platzi.status_code == 200:
    print("Aquí tienes lo que buscas")
elif response_platzi.status_code == 400:
    print("Ups, no puedo darte nada en el momento. Nosotros nunca paramos de mejorar <3")
```

Un artículo para profundizar en cómo manejar la librería request y como manejar los status code:
Request Tutorial

### HTML

En la web

HTML es para la estructura

CSS para los estilos

Javascript para las interacciones

```html
<script> hace referencia a un código ejecutable
<meta> aporta información extra al documento (metadatos)
<iframe> colocar paginas externas dentro de la página actual
```

RESUMEN: HTML ( Por Alejandro Giraldo Londoño)

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

HTML es una lenguaje que permite definir la estructura de una página web.
Estrucutra, estilo, partes interactivas. En el contexto de webscraping HTML es muy importante

Etiquetas está encerrado en angle brakets.<>
Una etiqueta peude contener a otras etiquetas, las etiquetas tienen atributos.

El conocimiento de los atributos será crucial porque con ellos podremos conectar el scraper para extraer información.

script Se utiliza para
insertar o hacer referencia a un script ejecutable dentro de un docuemnto HTML.

meta aporta información extra al documento, metadatos como autor, título, fehca, palabras clave
es de suma importancia para el navegador.

iframe Puedo anidar un elemento HTML
sobre otro elemento.

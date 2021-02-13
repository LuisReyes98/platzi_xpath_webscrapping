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

## Robots.txt: permisos y consideraciones al hacer web scraping

Se define un archivo llamado robots.txt en la raiz de la pagina web, para que la gente que hace web scraping no lo hagan tan extentido y no llegue afectar la experiencia de tus otros usuarios

Ejemplo robots.txt de platzi:

```txt
User-Agent: *
Allow: /
Allow: /conf/*
Allow: /conf-og/*
Disallow: /*/*/concepto/*/*/material/
Disallow: /login/facebook/
Disallow: /login/twitter/
Disallow: /*/*/live/
Disallow: /*/*/%7B%7Burl%20absolute=/
Disallow: /*/*/add_contribution/
Disallow: /mi-suscripcion/
Disallow: /r/
Disallow: /clases/*/nuevos_materiales/
Disallow: /kit-ui/
Disallow: /ui/
Disallow: /sfotipy/
Disallow: /streaming/*
Disallow: /payments/*
Disallow: /*/add_review/
Disallow: /*/save/
Disallow: /adquirir/*
Disallow: /comentario/
Disallow: /comment/
```

esto representa las reglas que los webscrapers deberian seguir al hacer webscraping en esta pagina

el robots.txt tambien es usado por google para saber que segmentos de la pagina web no se muestren

este archivo se define para que se sepa que esta permitido hacer webscraping en tu sitio web para evitar que se toque informacion sensible del sitio web

y como web scraper incumplir este archivo puede resultar en asuntos legales ya que estas incumpliendo las normas de uso del sitio web.

[Directivas para crear el archivo robots.txt](https://developers.google.com/search/docs/advanced/robots/create-robots-txt?hl=es&visit_id=637484788251299808-230564012&rd=1)

## Xpath

XML path language

Les comparto un recurso.

En http://labs.timtom.ch/library-webscraping/extras/xpath-cheatsheet.md.pdf pueden encontrar más información de XPath.

Xpath es para html lo que las expresiones regulares son para un texto

ya que XML y HTML comparten estructua en ambos se puede usar la misma logica para extraer informacion

ejemplo:

```xpath
//div/span//h1[@class="title"][1]
```

## Tipos de nodos de Xpath

Es una etiqueta HTML y todo su contenido

[Sitio web para practicar web scraping](http://toscrape.com/)

RESUMEN: Tipos de nodos

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Un nodo es lo mismo que la etiqueta y su contenido.
Un nodo puede contener a otros nodos.
En otras palabras Xpath nos permitirá navegar en los diferentes niveles de profundidad
deseados con el fin extraer información. Para describir los nodos y relaciones con Xpath se usan una
sintaxis de ejes.

Toscrape es un sandbox para practicar.

## Expresiones en XPATH

usando xpath en Javascript

```javascript
$x('expresion de xpath')

/**
 * Ejemplos realizados en la pagina
 * https://quotes.toscrape.com/
*/

$x('/') // el documento principal meta, style, html ,script

$x('/html') // el documento html

$x('//') //salto entre nodos

$x('//h1/a/text()') // accediendo el texto del h1

$x('//h1/a/text()').map(x => x.wholeText) // opteniendo el texto en javascript

$x('//span')  // seleccionar todos los elementos span

$x('//span/.')  // '/.' es el nodo actual siendo esto igual a hacer '//span'

$x('//span/..') // accediendo a todos los elementos padres de un span

// accediendo a atributos
$x('//span/@class') // extrae todo el contenido de todos los elementos class que esten en un elemento span
```

## Predicados en XPATH

```javascript
// [] se usa para predicados
$x('/html/body/div/div[1]') // en este caso se pide que solo traiga el primer elemento

$x('/html/body/div/div[last()]') // se pide el ultimo elemento de la lista

$x('//span[@class]') // solo los span que tenga una clase

$x('//span[@class="text"]') // solo los span que tenga la clase "text"

$x('//span[@class="text"]/text()').map(x => x.wholeText) // extrajendo todas la citas del sitio web
```

## Operadores en Xpath

```javascript
$x('//span[@class!="text"]') // todos los span que tenga una clase distinta de "text"

$x('/html/body/div/div[position()=1]') // trae los elementos en la posicion 1

$x('/html/body/div/div[position()>1]') // trae todos los elementos que se encuentran despues de la posicion 1

$x('//span[@class="text" and @class="tag-item"]') // trae los elementos que tengan como clase a "text" Y a "tag-item"

$x('//span[@class="text" or @class="tag-item"]') // trae los elementos que tengan como clase a "text" O a "tag-item"

$x('//span[not(@class)]') // trae todos los span que NO tengan una clase
```

## Wildcards en Xpath

```javascript
$x('/*') // trae todos los nodos que estan dentro del documento

$x('/html/*') // trae todos los nodos que estan inmediatamente despues del html

$x('//*') // trae todos los elementos que se encuentran en el documento

$x('//span[@class="text"]/@*') // trae todos los atributos de todos los span que tengan la clase texto

$x('/html/body//div/@*') // trae todos los atributos de todos los elementos div que estan dentro del body

$x('//span[@class="text" and @itemprop="text"]/*') // en este caso no trae nada ya que adentro solo hay texto plano no hay nodos

$x('//span[@class="text" and @itemprop="text"]/node()') // en todos los span que tengan como atributo class="text" and itemprop="text" trae todo el contenido esto es distinto a usar *, ya que aqui trae el contenido y texto plano de estos elementos a pesar que no estan dentro de un elemento html
```

## In-text search en Xpath

```javascript
// traer todos los autores que tienen un nombre que comienza por la letra A
$x('//small[@class="author" and starts-with(., "A")]/text()')
// starts-with(., "A")  el "." punto es para referirse al nodo actual , y A es el texto con que se compara que comienze

$x('//small[@class="author" and starts-with(., "A")]/text()').map(x=>x.wholeText) // viendo el texto de los autores que inician con la letra A

// autores que el nombre contenga Ro
$x('//small[@class="author" and contains(., "Ro")]')

$x('//small[@class="author" and contains(., "Ro")]/text()').map(x=>x.wholeText) // viendo el texto

// autores que terminan en t
$x('//small[@class="author" and ends-with(., "t")]/text()') // esta función no funcionara en el navegador ya que en los navegadores esta xpath 1.0 y ends-with se agrego en xpath 2.0

// usando expreciones regulares
$x('//small[@class="author" and matches(., "A.*n")]/text()') // inicia con la letra A y termina con la letra n , tambien de xpath 2.0

```

## Xpath Axes

[Cheatsheet](https://devhints.io/xpath)

```javascript

$x('/html/body/div/self::div') // referiendose al mismo nodo div actual

$x('/html/body/div/.') // sugar syntax del ejemplo anterior

$x('/html/body/div/child::div') // trae los hijos del nodo div


$x('/html/body/div/descendant::div') // trae todos los descendientes de este nodo

$x('/html/body/div/descendant-or-self::div') //  trae el nodo actual y todos sus descendientes
```

## Aplicando lo aprendido

```javascript
// ejemplos de https://books.toscrape.com/index.html

$x('//article[@class="product_pod"]/h3/a/@title') // trayendo todos los titulos de los libros

$x('//article[@class="product_pod"]/h3/a/@title').map(x => x.value)

$x('//article[@class="product_pod"]/div[@class="product_price"]/p[@class="price_color"]/text()') // tdoos los precios de los libros

$x('//article[@class="product_pod"]/div[@class="product_price"]/p[@class="price_color"]/text()').map(x => x.wholeText)

$x('//div[@class="side_categories"]/ul[@class="nav nav-list"]/li/ul/li/a/text()') // todas las categorias de libros

$x('//div[@class="side_categories"]/ul[@class="nav nav-list"]/li/ul/li/a/text()').map(x => x.wholeText.trim())

// RETO

/*
Extraer descripcion de libros

https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html
*/
$x('//article[@class="product_page"]/p[position()=1]/text()')

$x('//article[@class="product_page"]/p[position()=1]/text()')[0].wholeText


/*
Extraer stock de libros
*/

$x('//table[@class="table table-striped"]/tbody/tr/td/.')[5]

$x('//table[@class="table table-striped"]/tbody/tr[6]/td/text()')[0].wholeText

```

## Recomendaciones legales

revisar el archivo robots.txt

revisar los permisos y terminos de uso de la pagina a la cual le haras web scrapping

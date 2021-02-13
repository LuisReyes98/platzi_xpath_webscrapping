# Xpath de larepublica

url: https://www.larepublica.co/

- Links de noticias en el home

```xpath
/html//div[contains(@class,"H_img_title") or contains(@class,"V_Title_Img")]//h2/a/@href
```

- Titulo de una noticia específica

```xpath
//div[contains(@class,"OpeningPostNormal")]//h2/a/text()


//div[@data-epica-module-name="Contenido"]//h2[@style="font-size: 45px; line-height: 49px;"]/a/text()

$x('//h2/node()/text()')
```

- Resumen de una noticia específica

```xpath
//div[@class="lead"]/p/text()
```

- Cuerpo de la noticia

```xpath
//div[@class="html-content"]/p[not(@class)]/text()
```

import requests
import lxml.html as html
import os
import datetime


HOME_URL = 'https://www.larepublica.co/'

# XPATH_LINK_TO_ARTICLES = '//div[contains(@class,"H_img_title") or contains(@class,"V_Title_Img")]//h2/a/@href'

XPATH_LINK_TO_ARTICLES = '//h2/a/@href'

# XPATH_TITLE = '//div[contains(@class,"OpeningPostNormal")]//h2/a/text()'

# XPATH_TITLE = '//div[@data-epica-module-name="Contenido"]//h2[@style="font-size: 45px; line-height: 49px;"]/a/text()'
# XPATH_TITLE = '//h2/node()/text()'

# XPATH_TITLE = '//div/h2[@style="font-size: 45px; line-height: 49px;"]/a/node()'
XPATH_TITLE = '//div/h2/a[contains(@class,"Sect")]/text()'

XPATH_SUMMARY = '//div[@class="lead"]/p/text()'

XPATH_BODY = '//div[@class="html-content"]/p[not(@class)]/text()'


def parse_news(link, today):
  try:
    response = requests.get(link)
    if response.status_code == 200:
      notice = response.content.decode('utf-8')
      parsed = html.fromstring(notice)
      # print(link)

      try:
        title = parsed.xpath(XPATH_TITLE)[0]
        # print(title)

        title = title.replace('\"', '')
        summary = parsed.xpath(XPATH_SUMMARY)[0]
        body = parsed.xpath(XPATH_BODY)
      except IndexError:
        return

      print(title)

      with open(f'./news/{today}/{title}.txt', 'w', encoding='utf-8') as f:
        f.write(title)
        f.write('\n\n')
        f.write(summary)
        f.write('\n\n')
        for p in body:
          f.write(p)
          f.write('\n')

    else:
      raise ValueError(f'Error: {response.status_code}')
  except ValueError as ve:
    print(ve)


def parse_home():
  try:
    response = requests.get(HOME_URL)
    if response.status_code == 200:
      home = response.content.decode("utf-8")
      parsed = html.fromstring(home)
      links_to_news = parsed.xpath(XPATH_LINK_TO_ARTICLES)

      today = datetime.date.today().strftime("%d-%m-%Y")
      if not os.path.isdir(f'news/{today}'):
        os.mkdir(f'news/{today}')

      for link in links_to_news:
        parse_news(link, today)

    else:
      raise ValueError(f'Error: {response.status_code}')
  except ValueError as ve:
    print(ve)

def run():
  parse_home()


if __name__ == "__main__":
  run()

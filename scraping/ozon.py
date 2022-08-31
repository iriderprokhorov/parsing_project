import json
from datetime import datetime, date
import locale

locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")

from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time


URL = "https://seller.ozon.ru/news/"
URL_ITEM = "https://seller.ozon.ru/"


options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
)
options.add_argument("--disable-blink-features=AutomationCntroled")


s = Service(executable_path="/home/nickolai/Dev/scrap/chromedriver")
driver = webdriver.Chrome(service=s, options=options)


def scrap_url(url):
    try:
        driver.get(url)
        page_source = driver.page_source
        time.sleep(10)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    return page_source


parsed = BeautifulSoup(
    scrap_url("https://seller.ozon.ru/news/"), "html.parser"
)
news_dict = {}
tag_ext = "ozon"
i = 0
current_year = str(date.today().year)
a_tag = parsed.findAll("div", attrs={"class": "news-card"}, limit=10)
for div in a_tag:
    href = urljoin(URL_ITEM, div.a["href"])
    title = div.a.find(class_="news-card__title")
    pub_date = div.a.find(class_="news-card__date")
    tags_int = div.a.findAll(class_="news-card__mark")
    news_dict["title"] = title.get_text().replace("\n      ", "")
    pub_date = datetime.strptime(pub_date.get_text() + current_year, "%d %B%Y")
    news_dict["pub_date"] = str(pub_date)
    news_dict["tag_ext"] = tag_ext
    tags_list = []
    # tags = tags_int.get_text().split()
    for each in tags_int:
        if each:
            tags_list.append({"name": each.get_text()})
    news_dict["tags"] = tags_list
    with open(
        "parsed_data_ozon",
        "a",
        encoding="utf-8",
    ) as fp:
        json.dump(news_dict, fp, ensure_ascii=False, indent=4)
        fp.write(",\n")
    i = i + 1

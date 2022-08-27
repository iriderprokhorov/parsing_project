import json
import sys
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

URL = "https://market.yandex.ru/partners/news"
URL_ITEM = "https://market.yandex.ru/"


def scrap_url(url):
    try:
        response = requests.get(url)
    except requests.RequestException as error:
        print(f"не удалось открыть страницу: {URL}. Причина: {error}")
        sys.exit(1)

    if response.status_code != 200:
        raise ValueError(
            f"Код ответа сервера не соответствует ожидаемому при запросе {URL}"
        )
    return response.text


parsed = BeautifulSoup(scrap_url(URL), "html.parser")

news_dict = {}
tag_ext = "yandex"

a_tag = parsed.findAll("div", attrs={"class": "news-list__item"}, limit=10)
for div in a_tag:
    href = urljoin(URL_ITEM, div.a["href"])
    parsed_item = BeautifulSoup(scrap_url(href), "html.parser")
    tags_int = parsed_item.find(class_="news-info__tags")
    title = parsed_item.find(class_="news-info__title")
    pub_date = parsed_item.find("time")
    news_dict["title"] = title.get_text().replace("\xa0", " ")
    news_dict["pub_date"] = pub_date["datetime"]
    news_dict["tag_ext"] = tag_ext
    tags_list = []
    tags = tags_int.get_text().split("#")
    for each in tags:
        if each:
            tags_list.append({"name": each})
    news_dict["tags"] = tags_list
    with open(
        "parsed_data_yandex",
        "a",
        encoding="utf-8",
    ) as fp:
        json.dump(news_dict, fp, ensure_ascii=False, indent=4)
        fp.write(",\n")

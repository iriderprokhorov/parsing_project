# Scraping Yandex Market and Ozon
Проект содержит скрипты для скрапинга с сайтов яндекс маркета и озона. Расположены они в директории scraping и там же примеры их работы. После выполнения данных скриптов данные с сайтов выгружаются в файл в JSON формате. Далее эти данные можно занести в базу данных MySQL через API c использование эндпоинта news_bulk/ .


## Установка проекта локально

* Склонировать репозиторий на локальную машину:
```bash
git clone git@github.com:iriderprokhorov/parsing_project.git
cd parsing_project
```

* Cоздать и активировать виртуальное окружение:

```bash
python -m venv env
```

```bash
source env/bin/activate
```

* Cоздайте файл `.env`  с содержанием:

```
SECRET_KEY=секретный ключ django
DB_NAME=
DB_USER=
DB_PASSWORD=
```

* Перейти в директирию и установить зависимости из файла requirements.txt:

```bash
cd backend/
pip install -r requirements.txt
```

* Выполните миграции:

```bash
python manage.py migrate
```

* Запустите сервер:
```bash
python manage.py runserver
```

## Эндпоинты Api
Основной эндпоинт news/ - здесь реализованы все операции CRUD
Для загрузки большого объема используйте news_bulk/


Пример Get запроса к http://127.0.0.1:8000/api/news/

```bash
{
    "id": 9,
    "title": "Получайте больше заказов благодаря постоплате",
    "pub_date": "2022-08-12T13:07:17Z",
    "tag_ext": "yandex",
    "tags": [
        {
            "id": 4,
            "name": "DBS"
        },
        {
            "id": 12,
            "name": "Другое"
        },
        {
            "id": 11,
            "name": "Сводка"
        }
    ]
}
```

## "To do"
- [x] Добавить крутое README
- [ ] Всё переписать
- [ ] ...


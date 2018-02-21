# Crawler
Crawler - компонент предназначенный для перебора страниц Интернета с целью занесения информации о них в базу данных.

## Установка
    $ git clone https://github.com/MediaAnalyticsApp/crawler
    $ cd crawler
    $ pip3 install -r requirements.txt
    
## Использование
Crawler необходимо запускать с указанием ключей.
Для запуска парсинга sitemap файлов, используется ключ -s

    $ python3 crawler.py -s

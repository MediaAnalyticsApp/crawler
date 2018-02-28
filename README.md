# Crawler
Crawler - компонент предназначенный для перебора страниц Интернета с целью занесения информации о них в базу данных.

## Установка
    $ git clone https://github.com/MediaAnalyticsApp/crawler
    $ cd crawler
    $ pip3 install -r requirements.txt
    
## Использование
Для Crawler необходимо произвести минимальную настройку в файле conf/config.ini, следующую секцию

[DataBase]<br>
host = db.host<br>
port = 3306<br>
name = db.name<br>
user = db.user<br>
password = db.password<br><br>
Crawler использует схему БД расположенную в https://github.com/MediaAnalyticsApp/db <br>
Crawler необходимо запускать с указанием ключей.
Для запуска парсинга sitemap файлов, используется ключ -s

    $ python3 crawler.py -s

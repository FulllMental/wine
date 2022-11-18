# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Для того, чтобы раздел с товаром не был пустым, необходимо создать и заполнить `goods.xlsx` файл по принципу:
```commandline
  
1  |    Категория |            Название |            Сорт | Цена |                 Картинка |                Акция
-------------------------------------------------------------------------------------------------------------------
2  |   Белые вина |          Белая леди | Дамский пальчик |  399 |          belaya_ledi.png | Выгодное предложение
3  |      Напитки | Коньяк классический |                 |  350 | konyak_klassicheskyi.png |
4  |   Белые вина |           Ркацители |       Ркацители |  499 |            rkaciteli.png |
5  | Красные вина |       Черный лекарь |           Качич |  399 |        chernyi_lekar.png |
6  | Красные вина |           Хванчкара |   Александраули |  550 |           hvanchkara.png |
7  |   Белые вина |               Кокур |           Кокур |  450 |                kokur.png |
8  | Красные вина |        Киндзмараули |        Саперави |  550 |         kindzmarauli.png |
9  |      Напитки |                Чача |                 |  299 |               chacha.png | Выгодное предложение
10 |      Напитки |    Коньяк кизиловый |                 |  350 |     konyak_kizilovyi.png |
```
после чего поместить данный файл в одну директорию с `main.py`

### Необязательные для заполнения столбцы:
- "Сорт" - при отсутствии, надпись в блоке с товаром отсутствует
- "Акция' - при отсутсвии, пометка о выгодном предложении будет отстутствовать на товаре

## Запуск

- Скачайте код
- Для запуска используйте команду:
``` 
python3 main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000) или [localhost:8000](http://localhost:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Для того чтобы раздел с товаром не был пустым, необходимо создать и заполнить `goods.xlsx` файл по принципу:

| 1 | Категория | Название |Сорт |Цена |Картинка |Акция|
|---|-----------|---|---|---|---|---|
| 2 | _Белые вина_ |Белая<br/>леди|Дамский<br/>пальчик|399|belaya_ledi.png|Выгодное<br/>предложение|
| 3 | _Напитки_ |Коньяк<br/>классический|   |350|konyak_klassicheskyi.png||   |
| ... | ... | ... | ... | ... | ... | ... |


### Необязательные для заполнения столбцы:
- "Сорт" - Если этих данных по товару нет, то надпись в блоке с товаром отсутствует
- "Акция' - Если этих данных по товару нет, пометка о выгодном предложении будет отсутствовать на изображении

## Запуск

- Скачайте код
- Для запуска используйте команду, вместе с которой укажите директорию и название `.xlsx` файла с данными по товарам:
``` 
python3 main.py C:\...\myshop_site\goods.xlsx
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000) или [localhost:8000](http://localhost:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

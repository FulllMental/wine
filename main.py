import collections
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pprint import pprint

import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_lifetime():
    lifetime = datetime.now().year - 1920
    if lifetime % 100 in [number for number in range(11, 15)]:
        year_txt = ' лет'
    elif lifetime % 10 == 1:
        year_txt = ' год'
    elif lifetime % 10 in [2, 3, 4]:
        year_txt = ' года'
    else:
        year_txt = ' лет'
    return str(lifetime) + year_txt


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
wine_data = pd.read_excel('wine.xlsx').to_dict(orient='records')
drinks_data = pd.read_excel('wine2.xlsx', keep_default_na=False).to_dict(orient='records')


def get_all_drinks(drinks_data):
    all_drink_types = [drink['Категория'] for drink in drinks_data]
    categories = list(collections.Counter(all_drink_types))

    grouped_drinks = collections.defaultdict(list)
    for category in categories:
        for drink in drinks_data:
            if category not in drink['Категория']:
                continue
            grouped_drinks[category].append(drink)
    return grouped_drinks


pprint(get_all_drinks(drinks_data))


template = env.get_template('template.html')

rendered_page = template.render(
    lifetime=get_lifetime(),
    wine_data=wine_data
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()

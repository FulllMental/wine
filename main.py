import collections
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

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


def group_goods(shop_goods):
    all_goods_types = [product['Категория'] for product in shop_goods]
    categories = list(collections.Counter(all_goods_types))

    grouped_goods = collections.defaultdict(list)
    for category in categories:
        for product in shop_goods:
            if category not in product['Категория']:
                continue
            grouped_goods[category].append(product)
    return grouped_goods


if __name__ == '__main__':
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    shop_goods = pd.read_excel(f'goods.xlsx', keep_default_na=False).to_dict(orient='records')

    grouped_goods = group_goods(shop_goods)

    template = env.get_template('template.html')

    rendered_page = template.render(
        lifetime=get_lifetime(),
        grouped_goods=grouped_goods
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

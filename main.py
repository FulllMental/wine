from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

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

template = env.get_template('template.html')

rendered_page = template.render(
    lifetime=get_lifetime()
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()

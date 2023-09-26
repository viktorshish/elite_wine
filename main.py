from collections import defaultdict
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import click
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas


def get_delta_year():
    begin_date = datetime.date(year=1920, month=1, day=1)
    now_date = datetime.datetime.today()
    delta_year = now_date.year - begin_date.year

    return delta_year


def get_year_declension(delta_year):
    if delta_year % 100 in [11, 12, 13, 14]:
        return 'лет'
    elif delta_year % 10 == 1:
        return 'год'
    elif delta_year % 10 in [2, 3, 4]:
        return 'года'
    else:
        return 'лет'


def grouping_of_products(drinks):
    grouped_products = defaultdict(list)
    for category in drinks:
        grouped_products[category['Категория']].append(category)
    sorted_grouped_products = dict(sorted(grouped_products.items()))

    return sorted_grouped_products


def get_drinks(file_path):
    excel_data = pandas.read_excel(
        file_path,
        na_values='nan',
        keep_default_na=False
    )
    drinks = excel_data.to_dict(orient='records')

    return drinks


@click.command()
@click.option('--file_path', '-p', default='wine.xlsx',
              help='Specify file path and name file')
def main(file_path):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        delta_year=get_delta_year(),
        year_declension=get_year_declension(get_delta_year()),
        wines=grouping_of_products(get_drinks(file_path))
        )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()

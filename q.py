import os
import json
import jinja2
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked


def get_information_for_template():
    name_file = 'book_page_information.json'

    with open('site-example\statics\{}'.format(name_file), 'r', encoding='utf-8') as my_file:
        books_information = json.load(my_file)

    env = Environment(
        loader=jinja2.FileSystemLoader('site-example/statics/templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    number_pages = enumerate(list(chunked(books_information, 11)), 1)
    for i, q in number_pages:
        print(i)
        print(q)#


if __name__ == '__main__':
    get_information_for_template()
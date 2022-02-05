import os
import json
import jinja2
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked
from itertools import count

def get_rendered_page():
    name_file = 'book_page_information.json'

    with open('site-example\statics\{}'.format(name_file), 'r', encoding='utf-8') as my_file:
        books_information = json.load(my_file)

    env = Environment(
        loader=jinja2.FileSystemLoader('site-example/statics/templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    number_pages = enumerate(list(chunked(books_information, 10)), 1)

    for page_number, part_of_books in number_pages:
        rendered_page = template.render(
            books_information=list(chunked(part_of_books, 2)),
            page_number=page_number,
            number_pages=5
            )
        with open(('site-example/pages/index{}.html').format(page_number), 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == '__main__':
    os.startfile('main.py')

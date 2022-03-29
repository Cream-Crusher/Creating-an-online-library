import os
import json
import jinja2
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked


def get_processed_books(num = 10):
    file_name = 'book_page_information.json'
    
    with open(os.path.join('site-example', 'statics', '{}'.format(file_name)), 'r', encoding='utf-8') as file:
        books = json.load(file)

    processed_books = list(chunked(books, num))
    return processed_books


def get_template():
    env = Environment(
        loader=jinja2.FileSystemLoader(os.path.join('site-example', 'statics', 'templates')),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    return template


def get_rendered_page():
    template = get_template()
    processed_books = get_processed_books()
    pages_number = len(processed_books)

    for page_number, books in enumerate(processed_books, 1):

        rendered_page = template.render(
            books=list(chunked(books, 2)),
            page_number=page_number,
            pages_number=pages_number,
            )

        with open(os.path.join('site-example', 'pages', 'index{}.html'.format(page_number)), 'w', encoding="utf8") as file:
            file.write(rendered_page)

    print("Site rebuilt")

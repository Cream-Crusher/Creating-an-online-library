import json
import jinja2
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked


def get_processed_books_and_template():
    file_name = 'book_page_information.json'

    with open('site-example\statics\{}'.format(file_name), 'r', encoding='utf-8') as my_file:
        books_information = json.load(my_file)

    env = Environment(
        loader=jinja2.FileSystemLoader('site-example/statics/templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    books_num = 10
    template = env.get_template('template.html')
    processed_books = list(chunked(books_information, books_num))
    return template, processed_books


def get_rendered_page():
    template, processed_books = get_processed_books_and_template()
    pages_number = len(processed_books)

    for page_number, books_information in enumerate(processed_books, 1):
        rendered_page = template.render(
            books_information=list(chunked(books_information, 2)),
            page_number=page_number,
            pages_number=pages_number
            )

        with open(('site-example/pages/index{}.html').format(page_number), 'w', encoding="utf8") as file:
            file.write(rendered_page)

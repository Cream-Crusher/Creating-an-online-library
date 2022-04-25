import os
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked


def get_processed_books():
    maximum_page_books_number = 10
    file_name = 'book_page_information.json'
    path_a_file = os.path.join('site-example', 'media', file_name)

    with open(path_a_file, 'r', encoding='utf-8') as file:
        books = json.load(file)

    processed_books = list(chunked(books, maximum_page_books_number))
    return processed_books


def get_template():
    env = Environment(
        loader=FileSystemLoader(os.path.join('site-example', 'templates')),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    return template


def rendered_pages():
    template = get_template()
    processed_books = get_processed_books()
    pages_number = len(processed_books)

    for page_number, books in enumerate(processed_books, 1):

        rendered_page = template.render(
            books=list(chunked(books, 2)),
            page_number=page_number,
            pages_number=pages_number,
        )
        path_a_file = os.path.join('site-example', 'pages', 'index{}.html'.format(page_number))

        with open(path_a_file, 'w', encoding="utf8") as file:
            file.write(rendered_page)

    print("Site rebuilt")

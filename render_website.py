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
    processed_books_information = enumerate(list(chunked(books_information, 10)), 1)
    #num_page = max(processed_books_information)[0]
    return template, processed_books_information


def get_rendered_page():
    template, processed_books_information = get_information_for_template()

    for number_page, books_information in processed_books_information:

        rendered_page = template.render(
            books_information=list(chunked(books_information, 2)),
            number_page=number_page,
            num_page=5#num_page
            )
        with open(('site-example/pages/index{}.html').format(number_page), 'w', encoding="utf8") as file:
            file.write(rendered_page)

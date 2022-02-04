import os
import json
import jinja2
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked
from itertools import count

def get_rendered_page():
    name_file = 'book_page_information.json'

    with open(name_file, 'r', encoding='utf-8') as my_file:
        books_information = json.load(my_file)

    env = Environment(
        loader=jinja2.FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    books_information = list(chunked(books_information, 10))
    
    for num, part_of_books in enumerate(books_information, 1):
        if num <= 1:
            path_file = 'pages/index'
        else:
            path_file = 'index'

        rendered_page = template.render(
            books_information=list(chunked(part_of_books, 2)),
            path_file=path_file,
            id_num=num,
            num_pages=5 #добавить счет страниц
            )
        with open(('pages/index{}.html').format(num), 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == '__main__':
    os.startfile('main.py')

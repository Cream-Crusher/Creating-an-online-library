import os
from livereload import Server
from render_website import rendered_pages


server = Server()
server.watch(os.path.join('site-example', 'templates', 'template.html'), rendered_pages)

server.serve(root='.')

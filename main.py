import os
from livereload import Server
from render_website import get_rendered_page


server = Server()
server.watch(os.path.join('site-example', 'templates', 'template.html'), get_rendered_page)

server.serve(root='.')

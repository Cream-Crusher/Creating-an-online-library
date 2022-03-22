from livereload import Server
from render_website import get_rendered_page


server = Server()
server.watch('site-example/statics/templates/template.html', get_rendered_page)

server.serve(root='.')

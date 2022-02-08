from livereload import Server
from render_website import get_rendered_page


def rebuild():
    print("Site rebuilt")

server = Server()
server.watch('site-example/statics/templates/template.html', get_rendered_page, rebuild())
server.serve(root='.')

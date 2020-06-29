from src.bingo import func
from jinja2 import Template

template = Template(open('src/plantilla.j2').read())
file = open("bingo.html", "w")
file.write(template.render(tabla = func()))
file.close()

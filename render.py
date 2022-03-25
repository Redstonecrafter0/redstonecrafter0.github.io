import os
import json
import shutil
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('render', 'src'),
    autoescape=select_autoescape()
)

try:
    shutil.rmtree('out')
except:
    pass

os.mkdir('out')

with open('src/sites.json') as f:
    sites = json.load(f)
    for i in sites:
        with open(f'out/{i}', 'w') as out:
            out.write(env.get_template(i).render())

shutil.copytree('src/static', 'out/static')

with open('out/.nojekyll', 'w'):
    pass

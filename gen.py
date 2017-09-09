# -*- coding: utf-8 -*-
import os
import shutil
from io import open
from datetime import date
from markdown2 import markdown
from jinja2 import FileSystemLoader, Environment

from config import *

SITE = {}


# read files
for current in os.listdir(CFG['content']):
    fqp = os.path.join(CFG['content'], current)
    with open(fqp, 'r', encoding='utf-8') as infile:
        name = os.path.splitext(current)[0]
        SITE[name] = infile.read()


# convert markdown
for p in SITE:
    SITE[p] = markdown(SITE[p])


# apply template
SITE["index"] = ""

env = Environment(loader=FileSystemLoader(CFG['templates']))

for post in SITE:
    template = env.get_template("post.html")
    SITE[post] = template.render(
        post    = post,
        content = SITE[post],
        site    = SITE,
        author  = CFG['author'],
        year    = str(date.today().year),
        unlisted= CFG['unlisted'],
    )


# remove the build dir
if os.path.exists(CFG['build']):
    shutil.rmtree(CFG['build'])

# create build dir
os.makedirs(CFG['build'])

# copy assets (css, images, whatever)
for i in CFG['copy']:
    shutil.copytree(i, os.path.join(CFG['build'], i))

# write the pages
for post in SITE:
    fqp = os.path.join(CFG['build'], post+'.html')
    with open(fqp, "w", encoding="utf-8") as output:
        output.write(SITE[post])


print("finished")

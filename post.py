# -*- coding: utf-8 -*-
import os
import sys
from io import open
import shutil
from datetime import date

from config import CFG

title = 'Untitled'
if len(sys.argv) > 1:
    title = sys.argv[1]

fn = str(date.today()) + '--' + title.lower().replace(' ','-') + '.md'

fp = os.path.join(CFG['content'], fn)

content = """
<header>
	<h1>%TITLE%</h1>
	<strong><time>%DATE%</time></strong>
</header>

"""
content = content.replace('%TITLE%', title)
content = content.replace('%DATE%', date.strftime(date.today(), '%a, %d %b, %Y'))

with open(fp, 'w') as f:
    f.write(content)

os.system('%s %s' % (CFG['editor'], fp))

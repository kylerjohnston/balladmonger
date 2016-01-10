from . import main
from flask import render_template, url_for
import ujson
import random
from .. import poem_generator
from config import APP_ROOT
import os

with open(os.path.join(APP_ROOT,
        'balladmonger/printingpress/out/ngram_chain.json'), 'r') as r:
    reader = r.read()
chain = ujson.loads(reader)

@main.route('/')
@main.route('/index')
def flask_poem():
    length = random.randint(2,6)
    new_poem = poem_generator.Poem(chain, length)
    poem_lines = []
    for line in new_poem.lines:
        poem_lines.append(line)
    img_name = url_for('static', filename='img/img{}.png'.format(str(random.randint(1,11))))
    return render_template('index.html', lines = poem_lines,
                            img_name = img_name)

@main.route('/about')
def sources():
    return render_template('about.html')


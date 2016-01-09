from . import main
from flask import render_template, url_for
import ujson
import random
from .. import poem_generator

with open('balladmonger/ngram_chain.json', 'r') as r:
    reader = r.read().decode('utf-8')
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


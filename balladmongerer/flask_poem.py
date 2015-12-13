from balladmongerer import app
from flask import render_template
try:
    import cPickle as pickle
except:
    import pickle
import poem_generator
import random

@app.route('/')
@app.route('/index')
def flask_poem():
    with open('balladmongerer/ngram_chain.p', 'rb') as r:
        chain = pickle.load(r)
    length = random.randint(3,7)
    new_poem = poem_generator.Poem(chain, length)
    poem_lines = []
    for line in new_poem.lines:
        poem_lines.append(line.decode('utf-8'))
    img_name = "/static/img/img{}.png".format(str(random.randint(1,11)))
    return render_template('index.html', lines = poem_lines,
                            img_name = img_name)

@app.route('/about')
def sources():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')

if __name__ == '__main__':
    app.run()

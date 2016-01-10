#!/usr/bin/env python

import os
from balladmonger import create_app
from flask.ext.script import Manager
from config import APP_ROOT

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

@manager.command
def printrun():
    from balladmonger.printingpress import publisher, ngram_dict
    print('Making training text...')
    publisher.make_training_text()
    ngram = ngram_dict.nGramDict()
    ngram.generate_list(os.path.join(APP_ROOT,
        'balladmonger/printingpress/out/trainingtext.txt'))
    ngram.writeout()

if __name__ == '__main__':
    manager.run()

from flask import Flask
app = Flask(__name__)
from balladmongerer import flask_poem

if __name__ == '__main__':
    app.run()

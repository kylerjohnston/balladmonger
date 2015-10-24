try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    'description': 'A 21st-century early modern ballad generator',
    'author': 'Kyle Johnston',
    'author_email': 'kylerjohnston@gmail.com',
    'install_requires': ['nose', 'Flask', 'pickle', 'sys', 'os.path'],
    'packages': ['balladmongerer'],
    'name': 'balladmongerer'
}

setup(**config)

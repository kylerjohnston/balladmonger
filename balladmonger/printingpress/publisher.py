import os, re
import nltk
from .excludes import exclusions
from config import APP_ROOT

textout = os.path.join(APP_ROOT,
    'balladmonger/printingpress/out/trainingtext.txt')

class SourceText:
    def __init__(self, filepath):
        try:
            with open(filepath, 'r') as f:
                self.text = f.read()
        except:
            print('Error: {} not found.'.format(filepath))
            sys.exit(0)
        for pattern in exclusions:
            expression = re.compile(pattern, re.MULTILINE)
            self.text = expression.sub(' ', self.text)
        self.text = re.sub(r'(---|--)', '&mdash;', self.text)
        self.text = re.sub(r'\s+\.', '\.', self.text)
        self.text = re.sub(r'\b\.\.\s', '.', self.text)
        self.text = re.sub(r'\s+', ' ', self.text)
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        self.sentences = tokenizer.tokenize(self.text)
        for i in range(len(self.sentences)):
            self.sentences[i] = 'BEGIN NOW ' + self.sentences[i] + ' END'

    def writeout(self):
        with open(textout, 'a') as f:
            for sentence in self.sentences:
                f.write(sentence + '\n')

def make_training_text():
    f = open(textout, 'w').close()
    files = os.listdir(os.path.join(APP_ROOT,
            'balladmonger/printingpress/in/'))
    for filename in files:
        print("Making {}".format(filename))
        text = SourceText(os.path.join(APP_ROOT,
            'balladmonger/printingpress/in/' + filename))
        print("Writing {}".format(filename))
        text.writeout()

if __name__ == '__main__':
    make_training_text()

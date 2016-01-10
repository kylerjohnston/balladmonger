import sys
import os.path
import ujson
from config import APP_ROOT

class nGramDict:
    def __init__(self, json=True):
        nGramDict.chain = {}

    def add_keys(self, words):
        for word1, word2, word3 in self.generate_trigrams(words):
            key = "{0} {1}".format(word1.lower(), word2.lower())
            if key in self.chain:
                self.chain[key].append(word3)
            else:
                self.chain[key] = [word3]

    def generate_list(self, filepath):
        with open(filepath, 'r') as f:
            for line in f.readlines():
                words = line.split()
                self.add_keys(words)

    def generate_trigrams(self, words):
        if len(words) < 3:
            return
        for i in range(len(words) - 2):
            yield(words[i], words[i + 1], words[i + 2])

    def writeout(self):
        with open(os.path.join(APP_ROOT,
                'balladmonger/printingpress/out/ngram_chain.json'), 'w') as f:
            f.write(ujson.dumps(self.chain))

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("Need a file argument.")
        sys.exit(0)
    else:
        fpath = sys.argv[1]
        if(os.path.isfile(fpath)):
            ngram_dict = nGramDict()
            ngram_dict.generate_list(fpath)
            ngram_dict.writeout()
        else:
            print("File not found.")
            sys.exit(0)

try:
    import cPickle as pickle
except:
    import pickle
import random

class Poem:
    def __init__(self, ngrams, length = 300):
        self.chain = ngrams
        self.words = []
        sword1 = 'begin'
        sword2 = 'now'
        sents = 0
        while sents <= length:
            sword1, sword2 = sword2, random.choice(self.chain[sword1.lower(), sword2.lower()])
            if sword1.lower() == 'now':
                sword2 = sword2[0].upper() + sword2[1:]
            if sword2.lower() == 'end':
                sword1, sword2 = 'begin', 'now'
                sents += 1
            else:
                self.words.append(sword2)
        self.make_lines()

    def make_lines(self):
        self.lines = []
        p = 0
        while len(self.words) - p > 1:
            line_length = random.randint(4, 8)
            if line_length > len(self.words):
                line_length = len(self.words)
            line = ' '.join(str(v) for v in self.words[p:p+line_length])
            self.lines.append(line)
            p += line_length

if __name__ == '__main__':
    with open('ngram_chain.p', 'rb') as r:
        chain = pickle.load(r)
    new_poem = Poem(chain, 90)
    for line in new_poem.lines:
        print(line)

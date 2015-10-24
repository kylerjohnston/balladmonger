import pickle, sys, os.path, json

class nGramDict:
    def __init__(self):
        nGramDict.chain = {}

    def add_keys(self, words):
        for word1, word2, word3 in self.generate_trigrams(words):
            key = word1.lower() + word2.lower()
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
        with open("printingpress/out/ngram_chain.p", "wb") as f:
            pickle.dump(self.chain, f)
        # with open('printingpress/out/ngram_chain.json', 'wb') as f:
        #     json.dump(self.chain, f)

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

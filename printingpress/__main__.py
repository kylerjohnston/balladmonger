import publisher, ngram_dict, shutil

if __name__ == '__main__':
    publisher.make_training_text()
    ngram = ngram_dict.nGramDict()
    ngram.generate_list('printingpress/out/trainingtext.txt')
    ngram.writeout()
    shutil.copyfile('printingpress/out/ngram_chain.p', 'balladmongerer/ngram_chain.p')

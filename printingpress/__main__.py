import publisher, ngram_dict, shutil

if __name__ == '__main__':
    publisher.make_training_text()
    ngram = ngram_dict.nGramDict()
    ngram.generate_list('printingpress/out/trainingtext.txt')
    ngram.writeout()
    if ngram.json:
        shutil.copyfile('printingpress/out/ngram_chain.json', 
                        'balladmongerer/ngram_chain.json')
    else:
        shutil.copyfile('printingpress/out/ngram_chain.p',
                        'balladmongerer/ngram_chain.p')

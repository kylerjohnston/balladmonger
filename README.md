Train the script on a text by pointing ngram_dict.py at it. Example:

`$ python ngram_dict.py ~/balladmongerer/texts/winters_tale.txt`

This generates a file called `ngram_chain.p` which is a dictionary of bigrams, trigrams, and quadgrams from the text it was trained on that *balladmongerer* uses to generate its poems. Store `ngram_chain.p` in the `balladmongerer/balladmongerer` directory for the program to work.

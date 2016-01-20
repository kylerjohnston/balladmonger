# Balladmonger - README

## About

Balladmonger was written as a project for a graduate seminar on the interactions between Shakespearian texts and early modern ballads. Its purpose was to "remediate" *King Lear* into a ballad (well, multiple ballads) and a digital media object, interrogating in the process our ideas of what a work of literature is (can we call what Balladmonger produces remediations of *King Lear*?) and destabilizing (I hope) ideas of "authority" and "authorship." You can see the implementation of Balladmonger trained on *King Lear* at [http://balladmonger.kylerjohnston.com](balladmonger.kylerjohnston.com).

Of course, outside the context of my seminar Balladmonger is just a program that generates poems based on some texts you feed it. It could be trained on any texts.

## How it works

Balladmonger consists of two Python packages: `printingpress`, which cleans up the source texts and then trains a Markov chain model on them, and `balladmongerer`, which generates a poem based on the model trained by `printingpress` and formats it in HTML and CSS. The initial design of Balladmonger was heavily influenced by [this post](http://www.statsblogs.com/2014/02/20/how-to-fake-a-sophisticated-knowledge-of-wine-with-markov-chains/) on StatsBlog by Tony Fischetti. 

`printingpress` makes its model by extracting all possible trigrams from the training texts and putting them into a Python dictionary where the first two words act as a tuple key and the value is a list of all possible third words. So if we were training it on Taylor Swift:

> 'Cause the players gonna play, play, play, play, play
>
> And the haters gonna hate, hate, hate, hate, hate

we'd get something like:

```
ngram_dict = {
    ('cause', 'the'): ['players'],
    ('the', 'players'): ['gonna'],
    ('players', 'gonna'): ['play'],
    ('gonna', 'play'): ['play'],
    ('play', 'play'): ['play', 'play', 'play', 'and'],
    ('play', 'and'): ['the'],
    ('and', 'the'): ['haters'],
    ('the', 'haters'): ['gonna'],
    ('haters', 'gonna'): ['hate'],
    ('gonna', 'hate'): ['hate'],
    ('hate', 'hate'): ['hate', 'hate', 'hate']
}
```

There's no need to calculate probabilities of, e.g., the frequency of "and" occuring after the bigram "play play" since every instance of a word following "play play" is recorded in the list. So to generate a poem, all we have to do is randomly select a tuple key and then randomly select one item from its list of values. If we randomly select 'gonna play', 'play' is our only possible next value. Balladmonger then uses the last two words as a new key to select a new value. So 'play play' would be our new key, and now we have a list of four possible values to randomly select from, three of which are 'play' and one of which is 'and'.

`printingpress` does a little preprocessing on the texts, removing chapter headings and the like, and uses the [Natural Language Toolkit](http://www.nltk.org) library to try to infer where sentences end and begin before the model is generated, but essentially this is the way Balladmonger works.

## How to use Balladmonger
### Install
You should just be able to clone the repository. Take a look at `requirements.txt` to see what dependencies you'll need to install. It uses Python 2.7; probably won't work with Python 3 (though I haven't tested it).

### Training a model
`printingpress` expects your source texts to be in the directory `balladmonger/printingpress/in/`. (You'll have to create this directory yourself: I don't push it to Github because I don't own the texts I trained my model on). You might want to take a look at the source of `balladmonger/printingpress/excludes.py` which contains a list of regular expressions: `printingpress` loops through this list and removes all matches for each expression from the texts before training the model. You probably want to adjust it to be specific to whatever texts you're training it on. The regular expressions I have in there now were written specifically for the texts I trained my *Lear* model on.

Once you have that done, train your model by running the following command from the base `balladmonger/` directory:

`$ ./manage.py printrun`

This will generate a pickle file called `ngram_chain.p` which contains your Markov chain model dictionary. `printingpress` copies it automatically to the `balladmonger/balladmongerer/` directory where it's needed.

### Generating poems
Once you've run `printingpress` and you have an `ngram_chain.p` in the `balladmonger/balladmongerer/` directory, run:

`$ ./manage.py runserver` 

and your app should be running using Flask's built-in server at 127.0.0.1:5000. Refresh the page for a new poem!

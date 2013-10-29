"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import string
import random


def process_file(filename, skip_header=True):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    Returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = file(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        process_line(line, hist)
    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_line(line, hist):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    hist: histogram (map from word to frequency)
    """
    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    
    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        # update the histogram
        hist[word] = hist.get(word, 0) + 1


def most_common(hist):
    """Makes a list of the key-value pairs from a histogram and
    sorts them in descending order by frequency.

    hist: map from word to the number of times it appears

    returns: list of (word, frequency) pairs, sorted by frequency
    """
    t = []
    for key in hist:
        t.append((hist[key],key))

    t.sort(reverse = True)
    return t


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    
    hist: histogram (map from word to frequency
    num: number of words to print
    """
    t = most_common(hist)
    print 'The most common words are:'
    for freq, word in t[:num]:
        print word, '\t', freq


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries

    returns: new dictionary
    """
    res = {}
    for key in d1:
        if not key in d2:
            res[key] = None
    return res


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """                                                   
    total = sum(hist.values())

    where = random.randint(1,total)

    where_in_dict = 0

    for key in hist:
        where_in_dict = where_in_dict+hist[key]
        if where_in_dict >= where:
             return key


def get_prefixes(f,n_words):

    text= file(f)
    skip_gutenberg_header(text)

    t = []
    d = {}
    pref = ()

    for line in text:

        line.replace('-',' ')
        line.replace('_',' ')
        words  = line.split()

        for word in words:
            t.append(word)

    for word in t:
        if len(t) <2:
            break

        pref = tuple(t[0:n_words])

        if pref not in d:
            d[pref] = [t[n_words]]

        else:
            d[pref].append(t[n_words]);

        del(t[0])

    return d

def markov(f,len_res,len_phrase):
    prefix_dict = get_prefixes(f,len_phrase)

    key = prefix_dict.keys();
    which = random.randint(1,len(key))
    first = key[which]
    init = prefix_dict[first]

    suff = init[random.randint(0,len(init)-1)]

    text = []

    for i in range(0,len_res):

        begin_suff=list(first[1:])
        begin_suff.append(suff)

        first = tuple(begin_suff)
        
        init = prefix_dict[first]

        suff = init[random.randint(0,len(init)-1)]

        text.append(first[0])


    for word in text:
        print word,

markov('emma.txt',500,2)
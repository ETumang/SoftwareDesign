import anagram_sets
import shelve

"""Writes a dictionary of anagrams to a database.
"""
def store_anagrams():
    d = anagram_sets.all_anagrams('words.txt')

    #creates database
    db = shelve.open('anagrams.db' ,'c')

    for key in d:
        db[key] = d[key]

    db.close

"""Returns a list of anagrams of word 'word'.  Anagrams based on contents of words.txt and retreived from anagrams.db.

word: string

returns: list of strings
"""
def read_anagram(word):

    #generate sorted key from word
    t = list(word)
    t.sort()
    key = ''.join(t)

    db = shelve.open('anagrams.db')#open pre-stored database

    #if word not in database
    if not db.has_key(key):
        return []

    s = db[key]
    db.close
    return s

store_anagrams()
print read_anagram('pzst')

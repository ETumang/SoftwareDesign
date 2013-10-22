def make_word_list(f):
    """Reads lines from a file and builds a list using append.
    f: file
    returns: list of strings
    """
    t = []
    words = open(f)
    for line in words:
        s = line.strip()
        t.append(s)
    return t

"""Reads words from a file and returns a dictionary of anagrams.

f: file

return: dictionary of lists
"""
def anagram_set(f):
    wordlist = make_word_list(f)
    anagram_d = dict()

    for word in wordlist:
        sorttup = tuple(sorted(word))

        if sorttup in anagram_d:
            anagram_d[sorttup].append(word)

        else:
            anagram_d[sorttup] = [word]
        
    return anagram_d

"""Prints the values of a dictionary.

d: dictionary
"""
def print_contents(d):
    for key in d:
        if len(d[key]) >1:
            print d[key]

"""Prints the values of a dictionary in order by length.

d: dictionary
"""
def sort_dict_by_len(d):
    t = []
    for key in d:
        a_list = d[key]
        t.append((len(a_list),a_list))

    t.sort()
    for i in t:
        print i

"""Finds the largest group of anagrams of n letters.  If more than one group exists with the same length, it prints the 
first to appear in d.

d: dictionary of lists

n_letters: positive integer
"""
def find_bingo(d,n_letters):
    longest = []
    for key in d:
        a_list = d[key]
        if len(a_list) > len(longest):
            if len(a_list[0]) ==n_letters:
                longest = a_list

    print longest

find_bingo(anagram_set('words.txt'),8)


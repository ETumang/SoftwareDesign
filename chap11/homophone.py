from pronounce import read_dictionary


"""Finds all five-letter words whose last four letters 
and first and last three letters are a homophone of the original
word.
"""
def find_triplephone():

    d = dict()
    pro= read_dictionary();

    for line in (open('words.txt')):
        word = line.strip()
        d[word] = {}

    for key in d:
        if len(key) ==5:
            w1 = key[1:]
            w2 = key[0] + key[2:]

            if (w1 in pro)&(w2 in pro):
                
                if pro[w1]==pro[w2]== pro[key]:
                    print key
find_triplephone()
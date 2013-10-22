tested = {"":True}

words = open('words.txt')
d = {"":""}
for line in words:
    word = line.strip().lower()
    d[word] = word

"""Finds if a word is reducible- that is, if by removing one letter from it you get another word,
 and so on until you reach the empty string.

word: string

return: boolean
 """
def is_reducible(word):

    if word not in d:
        return False

    if word in tested:
        return tested[word]

    else:

        for i in range(0,len(word)):
            w = word[:i]+word[i+1:]

            tested[w] = is_reducible(w)
            
            if tested[w]:
                tested[word] = True
                return True

        tested[word] = False
        return False

"""Stores all reducible words in a list and prints the longest one, as well as its length."""
def find_reducibles():
    reducibles = []
    for key in d:
        if is_reducible(key):
            reducibles.append((len(d[key]),key))

    reducibles.sort()
    print reducibles[len(reducibles)-1]

"""Prints the various reductions made to a word to reach the empty string.

word: string

return: boolean
"""
def trace_reduction(word):
    if word not in d:
        return False

    if word in tested:
        return tested[word]

    else:

        for i in range(0,len(word)):
            w = word[:i]+word[i+1:]

            tested[w] = trace_reduction(w)
            
            if tested[w]:
                print w
                tested[word] = True
                return True

        tested[word] = False
        return False

trace_reduction('complecting')

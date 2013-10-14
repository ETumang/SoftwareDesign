from bisect import bisect_left
import time

def make_word_list1(f):
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


def is_in_list(L,word):
'''Finds whether a word is included in a list.

L: list 
word: string

return: boolean
'''
    i = bisect_left(L,word)
    if i<len(L):
        if L[i] == word:
            return True

    return False

def is_in_list2(L,word):
'''Finds whether a word is included in a list.

L: list of strings
word: string

return: boolean
'''
    for s in L:
        if s == word:
            return True
        return False

def reverse_pair(L):
'''Prints a list of words which, when reversed, are also words.

L: list of strings
'''
    for word in L:
        if is_in_list(L, word[::-1]):
            print word+" "+word[::-1]

def interlock(L):
'''Prints pairs of words which, when interleaved, form another word.

L: list of strings
'''
    for word in L:
        
        s1 = ""
        s2 = ""
        for i in range(0,len(word)):
            if i%2 ==0:
                s1 += word[i]
            else:
                s2 += word[i]

        if is_in_list(L,s1)&is_in_list(L,s2):
            print s1 + " " +s2 + " "+ word

def interlock_many(L,n):
'''Prints words which can be de-interleaved to form n separate words.

L: list of strings
n: number of words included in each interleaved word
'''
    for word in L:
        is_interlock =True
        for i in range(0,n):
            w = word[i::n]
            if not (is_in_list(L,w)):
                is_interlock = False
                break
        if is_interlock:
            print word


'''
start_time = time.time()
t = ["and","hello","what","where","xylophone"]
elapsed_time = time.time() - start_time

print is_in_list(t, "where")
print elapsed_time, 'seconds'

start_time = time.time()
elapsed_time = time.time() - start_time

print is_in_list2(t,"where")
print elapsed_time, 'seconds'
'''
t = make_word_list1('words.txt')
interlock_many(t,3)
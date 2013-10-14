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
    i = bisect_left(L,word)
    if i<len(L):
        if L[i] == word:
            return True

    return False

def is_in_list2(L,word):
    for s in L:
        if s == word:
            return True
        return False

def reverse_pair(L):
    for word in L:
        if is_in_list(L, word[::-1]):
            print word+" "+word[::-1]

def interlock(L):
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
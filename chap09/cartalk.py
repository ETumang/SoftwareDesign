def find_double(word):
'''Determines if a word contains three repeated letters in a row.

word: string

return: boolean
'''
    if len(word)<6:
        return False
    double = False
    for i in range(0,len(word)-5):
        if (word[i] == word[i+1]) & (word[i+2]== word[i+3]) & (word[i+4] ==word[i+5]):
                    return True

    return False

def find_words():
'''Scans words.txt for a word with three double letters.'''
    words = open('words.txt')

    for line in words:
        s = line.strip()
        if find_double(s):
            print s


def is_palindrome(s):
'''Checks if s is a palindrome.

s: string

return: boolean
'''
    return s == s[::-1]

def find_nums():
'''Finds a 6-digit number that is a palindrome, with num-2 having a palindromic final 5 digits and num-3 
having a palindromic final 4 digits.'''

    for i in range(000000,999999):
        test = i
        s = str(test).zfill(6)
        if is_palindrome(s):
            test = test-2
            s = str(test)[1:].zfill(5)
            if is_palindrome(s):
                test = test-1
                s = str(test)[2:].zfill(4)
                if is_palindrome(s):
                    print test

def is_reverse(word1, word2):
'''Returns if word 1 is word 2, reversed.

word1: string

word2: string

return: boolean
'''

    return word1[::-1] == word2

def find_ages():
'''Finds an age meeting the criteria for exercise 9.9.'''

    for diff in range(10,60):

        count = 0

        for young in range(0,99):
            older = diff + young
            if older > 99:
                break

            s_older = str(older).zfill(2)
            younger = str(young).zfill(2)
        
            if is_reverse(s_older,younger):
                count = count + 1

                
        if count > 7:
            num =0
            for age in range(10,99):
                elder = str(age+diff)
                younger = str(age)

                if is_reverse(elder, younger):
                    num = num+1
                    

                if num == 5:
                    print younger
                    break

            








"""Module that provides is_palindrome.

Author of is_palindrome: you
"""

def first(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[0]


def last(word):
    """Returns the last character of a word.

    word: string

    returns: length 1 string
    """
    return word[-1]


def middle(word):
    """Returns all but the first and last character of a word.

    word: string

    returns: string
    """
    return word[1:-1]


def is_palindrome(word):
    """Returns true if a word is a palindrome and false if it
    is not. 
     
    word:string

    returns:string
    """
    if len(word)>2 and not is_palindrome(middle(word)):
        return False
    else:
        return first(word) == last(word)

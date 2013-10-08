def rotate_word(word, rot):
""" 'Rotates' the letters of a world by rot indices, looping back when z is reached.

word: string

rot: int

return: string
"""
    word = word.lower()
    w = ""
    print w

    for c in word:
        n_in_alpha = ord(c)-97
        shift = (n_in_alpha + rot)%26
        print shift
        w = w + chr(97+shift)
    return w

print rotate_word("cheer",7)

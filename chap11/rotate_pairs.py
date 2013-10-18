def rotate_word(word, rot):
    word = word.lower()
    w = ""

    for c in word:
        n_in_alpha = ord(c)-97
        shift = (n_in_alpha + rot)%26
        
        w = w + chr(97+shift)
    return w

"""Finds pairs of words in a filethat can be rotated by some
amount to form each other."""
def rotate_pairs(f):
    d = dict()
    words = open(f)
    for line in words:
        word = line.strip()
        d[word] = {}

    for key in d:
        for n in range(1,24):
            rot = rotate_word(key,n)
            if rot in d:
                print key+ " "+rot

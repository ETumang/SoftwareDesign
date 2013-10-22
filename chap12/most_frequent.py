def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) +1
    return d

def most_frequent(s):
    freqs = sorted(tuple(histogram(s)))
    print freqs





def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) +1
    return d

def reverse_lookup(d,v):
    t = []
    for k in d:
        if d[k] == v:
            t.append(k)

    return t

d = {'where':'this','here':'gone','what':'gone'}

print reverse_lookup(d, 'gone')
print reverse_lookup(d, 'that')
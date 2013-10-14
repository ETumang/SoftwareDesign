def nested_sum(L):
    total = 0
    for set in L:
        total += sum(set)

    return total

def cumulative_sum(L):
    N = []
    for i in range (1,len(L)+1):
        N.append(sum (L[:i]))
    return N



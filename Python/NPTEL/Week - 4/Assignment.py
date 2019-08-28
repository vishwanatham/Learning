def frequency(I):
    d = dict.fromkeys(I)
    r = {}
    for i in d.keys():
        count = 0
        for j in I:
            if i == j:
                count += 1
        r[str(i)] = count
    minimum = min(r.values())
    maximum = max(r.values())
    minlist = [int(key) for key, value in r.items() if value == minimum]
    maxlist = [int(key) for key, value in r.items() if value == maximum]
    return ((sorted(minlist), sorted(maxlist)))


def onehop(l):
    r = []
    for (i, j) in l:
        for (m, n) in l:
            if (i, j) != (m, n):
                if i != n and j == m and not(r.__contains__((i, n))):
                    r.append((i, n))
    return sorted(r)
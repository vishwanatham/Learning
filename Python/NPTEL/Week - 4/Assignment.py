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

l = [(1,2), (3,2)]
r = []
for (i,j) in l:
    for (m,n) in l:
        # print(i, j, m, n)
        if ( (i, j) != (m, n) ):
            if i == m and not( r.__contains__((j,n))) and not(r.__contains__((n,j))):
               r.append(sorted(j, n))
            elif i == n and not( r.__contains__((j,m))) and not(r.__contains__((m,j))):
                r.append(sorted(j, m))
            elif j == m and not( r.__contains__((i,n))) and not(r.__contains__((n,i))):
                r.append(sorted(i, n))
            elif j == n and not( r.__contains__((i,m) )) and not(r.__contains__((m,i))):
                r.append((i, m))
print(r)

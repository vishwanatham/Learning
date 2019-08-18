def expanding(l):
    prevdiff = 0
    for i in range(0, len(l)-1):
        diff = abs(l[i] - l[i+1])
        if i > 0:
            if prevdiff >= diff:
                return False
        prevdiff = diff
    return True


def accordian(l):
    prevdiff = 0
    id = ''
    for i in range(0, len(l)-1):
        diff = abs(l[i] - l[i+1])
        if i > 0:
            if prevdiff > diff and (id == '' or id == 'i'):
                id = 'd'
            elif prevdiff < diff and (id == '' or id == 'd'):
                id = 'i'
            else:
                return False
        prevdiff = diff
    return True


def rotate(m):
    # To copy the nested list as values
    l = []
    for a in m:
        l.append(a[:])
    for i in range(0, len(m)):
        k = 0
        for j in range(len(m)-1, -1, -1):
            l[i][k] = m[j][i]
            k += 1
    return(l)


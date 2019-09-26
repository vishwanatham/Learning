#noofcolumns = int(input())
M = [[8, 6, 2, 3], [9, 7, 1, 2]]
#M.append(list(input().split(' ')))
#M.append(list(input().split(' ')))

#print(noofcolumns)
print(M)
o1 = 0
o2 = 0
r = []
for i in range(0, 4):
    if i == 0:
        r.append([1, abs(M[0][0]-M[0][1]) + abs(M[1][0]-M[1][1])])
        r.append([0, abs(M[0][0] - M[1][0])])
        print(r)
    else:
        for item in r:
            k = item[0]
            print(k)
            if (k >= i) and (k+2 < 3):
                r.append([k+2, abs(M[0][k+1]-M[0][k+2]) + abs(M[1][k+1]-M[1][k+2])])
                r.append([k+1, abs(M[0][k + 1] - M[1][k + 1])])
                print(r)

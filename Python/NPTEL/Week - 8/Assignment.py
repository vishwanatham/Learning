nc = int(input())
m = list()
m.append(list(map(int, input().strip().split(' '))))
m.append(list(map(int, input().strip().split(' '))))

r = []
fr = []
rl = []
ni = len(m[0]) - 1

fr.append([1, abs(m[0][0] - m[0][1]) + abs(m[1][0] - m[1][1])])
fr.append([0, abs(m[0][0] - m[1][0])])
for i in range(1, nc):
    try:
        r = fr.copy()
        fr.clear()
        for item in list(filter(lambda x: x[0] < ni, r)):
            k = item[0]  # Prev Position
            j = item[1]  # Previous Sum
            fr.append([k + 1, abs(m[0][k + 1] - m[1][k + 1]) + j])
            if k + 2 <= ni:
                fr.append([k + 2, abs(m[0][k + 1] - m[0][k + 2]) + abs(m[1][k + 1] - m[1][k + 2]) + j])
            r.clear()
        for l in [x[1] for x in fr if x[0] == ni]:
            rl.append(l)
    except MemoryError:
        print(fr)
        break
    else:
        break


print(max(rl))

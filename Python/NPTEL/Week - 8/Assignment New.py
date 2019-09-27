nc = int(input())
m = list()
m.append(list(map(int, input().strip().split(' '))))
m.append(list(map(int, input().strip().split(' '))))
s = abs(m[0][0] - m[1][0])
t = 0
for i in range(1, nc):
    vertical_tile = s + abs(m[0][i] - m[1][i])
    horizontal_tile = t + abs(m[0][i - 1] - m[0][i]) + abs(m[1][i - 1] - m[1][i])
    t = s
    s = max(vertical_tile, horizontal_tile)
print(s)

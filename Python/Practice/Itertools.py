from itertools import count, accumulate, product, takewhile, permutations, combinations


for i in range(1, int(2)+1):
    for j in combinations(sorted('HACK'), i):
        print(''.join(j))

plist = list()
for x in list(permutations('HACK', 2)):
    plist.append(''.join(x))

for x in sorted(plist):
    print(x)

for x in list(product([1, 2], [2, 3])):
    print(x, end=" ")

for x in count(1):
    print(x)
    if x == 5:
        break

numbers = list(accumulate(range(6)))

print(numbers)

print(list(takewhile(lambda x: x < 10, numbers)))



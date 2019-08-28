def InsertionSort(l):

    for sliceend in range(len(l)):
        pos = sliceend
        while pos > 0 and l[pos-1] > l[pos]:
            (l[pos-1], l[pos]) = (l[pos], l[pos-1])
            pos -= 1



import time

l = [2, 8, 4, 7, 13]
start = time.time()
InsertionSort(l)
print("Duration is ",  time.time() - start)
print(l)

l = list(range(1, 100, 2)) + list(range(0, 70, 2))
start = time.time()
InsertionSort(l)
print("Duration is ",  time.time() - start)
print(l)

l = list(range(5000, 0, -1))
start = time.time()
InsertionSort(l)
print("Duration is ",  time.time() - start)
print(l)

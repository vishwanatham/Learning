def SelectionSort(l):

    # Scan slices l[0:len(l)], l[1:len(l)]....
    for start in range(len(l)):

        # find the minimum position in the current slice
        minpos = start
        for i in range(start, len(l)):
            if l[i] < l[minpos]:
                minpos = i

        # ... and move it to start of the slice
        if start != minpos:
            (l[start], l[minpos]) = (l[minpos], l[start])


import time

l = [2, 8, 4, 7, 13]
start = time.time()
SelectionSort(l)
print("Duration is ",  time.time() - start)
print(l)

l = list(range(1, 100, 2)) + list(range(0, 70, 2))
start = time.time()
SelectionSort(l)
print("Duration is ",  time.time() - start)
print(l)

l = list(range(5000, 0, -1))
start = time.time()
SelectionSort(l)
print("Duration is ",  time.time() - start)
print(l)
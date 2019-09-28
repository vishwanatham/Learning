def merge_v1(A, B):
    (C, m, n) = ([], len(A), len(B))
    (i, j) = (0, 0)  # Current positions in A, B
    while i + j < m + n:
        if i == m:  # we copied everything from A to C, so we can now copy whatever is left in B to C.
            C.append(B[j])
            j += 1
        elif j == n:  # we copied everything from B to C, so we can now copy whatever is left in A to C.
            C.append(A[i])
            i += 1
        elif A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append((B[j]))
            j += 1
    return C

def merge(A, B):
    (C, m, n) = ([], len(A), len(B))
    (i, j) = (0, 0)  # Current positions in A, B
    while i + j < m + n:
        if i == m:  # we copied everything from A to C, so we can now copy whatever is left in B to C.
            C.extend(B[j:])
            return C
        elif j == n:  # we copied everything from B to C, so we can now copy whatever is left in A to C.
            C.extend(A[i:])
            return C
        elif A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append((B[j]))
            j += 1
    return C

def mergesort(A, left, right):
    if right - left <= 1:  # Base case, we reached the array of length 1
        return A[left:right]
    else:
        mid = (left + right)//2

    L = mergesort(A, left, mid)
    R = mergesort(A, mid, right)
    return merge(L, R)


print(mergesort([23, 12, 43, 22, 52, 1, 2, 100, 222, 11, 33], 0, 11))




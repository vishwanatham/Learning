# Quick sort in Python
def partition(array, first, last):
    (pivotvalue, leftmark, rightmark) = (array[first], first+1, last)
    done = False
    while not done:

        # Increase left mark as long as the value at that position is less than pivot & right mark is not crossed yet
        while leftmark <= rightmark and array[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        # Decrease the right mark as the value at that position is greater than pivot & left mark is not crossed yet
        while array[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            (array[leftmark], array[rightmark]) = (array[rightmark], array[leftmark])

    (array[first], array[rightmark]) = (array[rightmark], array[first])

    return rightmark

def quickSort(array, first, last):
    if first < last:
        splitpoint = partition(array, first, last)

        quickSort(array, first, splitpoint - 1)
        quickSort(array, splitpoint + 1, last)


data = [8, 7, 2, 1, 0, 9, 6]
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)

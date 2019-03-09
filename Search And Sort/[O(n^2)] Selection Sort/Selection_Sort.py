def swap(arr, pos1, pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp


def selection_sort(unsorted):
    for i in range(len(unsorted)):
        minval = unsorted[i]
        minpos = i
        for j in range(i, len(unsorted), 1):
            if unsorted[j] < minval:
                minval = unsorted[j]
                minpos = j
        swap(unsorted, i, minpos)
    print(unsorted)


selection_sort([5, 4, 3, 2, 1])

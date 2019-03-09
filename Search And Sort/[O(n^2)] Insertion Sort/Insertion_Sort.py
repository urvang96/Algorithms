def swap(arr, pos1, pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp


def insertion_sort(unsorted):
    for i in range(1, len(unsorted), 1):
        nextval = i
        for j in range(i-1, -1, -1):
            if unsorted[j] > unsorted[nextval]:
                swap(unsorted, nextval, j)
                nextval -= 1
            else:
                break
    print(unsorted)


insertion_sort([5, 4, 3, 2, 1])

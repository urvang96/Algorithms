def binary_search(sortedranges, find, start, end):

    midpoint = int((end+start) / 2)
    if find == sortedranges[midpoint]:
        return midpoint
    if find < sortedranges[midpoint]:
        return binary_search(sortedranges, find, start, midpoint)
    else:
        return binary_search(sortedranges, find, midpoint, end)


res = binary_search([1, 2, 3, 4, 5], 5, 0, 5)
print(res)

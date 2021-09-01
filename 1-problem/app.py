def isSubsequence(firstArray, seconArray):
    index = 0
    for each_item in firstArray:
        if index == len(seconArray):
            break
        if seconArray[index] == each_item:
            index = index + 1
    return index == len(seconArray)


first = [4, 3, 25, 6, -10, 8, 7, 22, 1]
second = [3, 6, -10, 8]
print(isSubsequence(first, second))
# program.py

def isSubsequence(firstArray, seconArray):
    index = 0
    for each_item in firstArray:
        if index == len(seconArray):
            break
        if seconArray[index] == each_item:
            index = index + 1
    return index == len(seconArray)


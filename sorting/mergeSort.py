import random

def merge(arr1, arr2):
    arr1 = arr1.sort()
    arr2 = arr2.sort()
    D = [0 for i in range(0, len(arr1) + len(arr2))]
    while arr1 != [] and arr2 != []:
        b = arr1[0]
        c = arr2[0]
        if b <= c:
            D.append(arr1.pop(0))
        else:
            D.append(arr2.pop(0))
    return D


def merge_sort(array):
    if len(array) == 1:
        return array
    m = len(array) // 2
    B = merge_sort(array[0:m])
    C = merge_sort(array[m + 1: len(array) - 1])
    mergeLists = merge(B, C)
    return mergeLists


testList = []
for i in range(0, 1000):
    testList.append(random.randint(1, 10))
print(testList)
print(merge_sort(testList))
def selectionSort(array):
    arr = array
    for i in range(0, len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

myArr = 'dkjgheildnbe'
myList = []
for char in myArr:
    myList.append(char)
myList = [1, 4, 2, 9, 8, 7, 11]
print(myList)
print(selectionSort(myList))
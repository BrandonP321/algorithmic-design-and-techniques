import time

def binary_search(arr, low, high, key):
    if high < low:
        return low - 1
    mid = low + ((high - low) // 2)
    if key == arr[mid]:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)


def binary(arr, key):
    low = 0
    high = len(arr) - 1
    while True:
        if high < low:
            return 'NOT_FOUND'
        mid = low + ((high - low) // 2)
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1


def lang_bin(arr, key):
    low = 0
    high = len(arr) - 1
    while True:
        if high < low:
            return 'NOT_FOUND'
        mid = low + ((high - low) // 2)
        if arr[mid][0] == key:
            return mid
        elif key < arr[mid][0]:
            high = mid - 1
        else:
            low = mid + 1


def lang_binary(arr, lang_arr, key):
    arr = sorted(arr)
    location = lang_bin(arr, key)
    if location == 'NOT_FOUND':
        return 'NOT_FOUND'
    word_location = arr[location][1]
    return lang_arr[word_location - 1]


def add_to_words(number, english_word, french_word):
    global french
    global english
    english.append((english_word, number))
    french.append(french_word)


mylist = [10, 20, 30, 40, 50, 60, 70]
mylist = []

for i in range(0, 100000, 10):
    mylist.append(i)

mykey = 40

print(binary_search(mylist, 0, len(mylist) - 1, mykey))

print(binary(mylist, mykey))


english = [('house', 1), ('chair', 2), ('desk', 3), ('book', 4), ('door', 5)]
spanish = ['casa', 'silla', 'escritorio', 'libro', 'puerta']
french = ['maison', 'chaise', 'bureau', 'livre', 'porte']

print(lang_binary(english, french, 'door'))

english = []

with open('french_words.txt', 'r') as french_file:
    file = french_file.readlines()
    print(file)
    french = []
    for phrase in file:
        phrase = phrase[0: -1]
        print(phrase)
        phrase = phrase.split("\t")
        add_to_words(phrase[0], phrase[2], phrase[1])

print(english)
print(french)

print(lang_binary(english, french, 'hello'))

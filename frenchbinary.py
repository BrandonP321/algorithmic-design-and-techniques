import time

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
    return lang_arr[int(word_location) - 1]


def linear_search(arr, lang_arr, key):
    for word in arr:
        if word[0] == key:
            return lang_arr[int(word[1]) - 1]
    return 'NOT_FOUND'


def add_to_words(number, english_word, french_word):
    global french
    global english
    english.append((english_word, number))
    french.append(french_word)


english = []
french = []

with open('french_words.txt', 'r') as french_file:
    file = french_file.readlines()

    for phrase in file:
        phrase = phrase[0: -1]
        phrase = phrase.split("\t")
        add_to_words(phrase[0], phrase[2], phrase[1])


word = input("What word: ")
while word != 'q':
    print(lang_binary(english, french, word))

    print(linear_search(english, french, word))

    word = input("What word: ")
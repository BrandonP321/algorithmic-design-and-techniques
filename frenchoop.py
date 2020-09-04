class French(object):

    @staticmethod
    def lang_search(english_list, french_list, key):
        english_list = sorted(english_list)
        location = binary_search(english_list, key)
        if location == 'NOT_FOUND':
            return 'NOT_FOUND'
        word_location = english_list[location][1]
        return french_list[int(word_location) - 1]

    @property
    def _phrases(self):
        with open('french_words.txt', 'r') as french_file:
            file = french_file.readlines()

            for phrase in file:
                phrase = phrase[0: -1]
                phrase = phrase.split("\t")
                add_to_words(phrase[0], phrase[2], phrase[1])


def binary_search(arr, key):
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


def add_to_words(number, english_word, french_word):
    english.append((english_word, number))
    french.append(french_word)
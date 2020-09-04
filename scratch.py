import random

# mylist = []
# for i in range(10000000):
#     mylist.append(random.randint(0, 1000000))
#
# with open('test.txt', 'w') as test_file:
#     print(mylist, file=test_file)

with open('test.txt', 'r') as test_file:
    for i in test_file:
        print(i + '\n')
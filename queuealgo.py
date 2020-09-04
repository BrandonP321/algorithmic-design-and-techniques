import random


def groups(li):
    li = sorted(li)
    groupings = {}
    start = 0
    for i in range(1, len(li)):
        groupings[i] = []

        for j in range(start, len(li)):
            if li[j] <= (li[start] + 2):
                groupings[i].append(li[j])
            else:
                start = j
                break
        if j == len(li) - 1:
            break

    return groupings


arr = [3, 3, 3, 4, 4, 5, 6, 6, 6, 7]

print(groups(arr))

test_list = []
for k in range(1000):
    test_list.append(random.randint(1, 22))
print(sorted(test_list))

test_groups = groups(test_list)
print(test_groups)

print()

for group in test_groups:
    print(test_groups[group][-1] - test_groups[group][0])

def largest(num):
    num_list = []
    for c in str(num):
        num_list.append(c)
    num_list.sort(reverse=True)
    return "".join(num_list)


print(largest(98961))
num = int(input("Enter a number: "))

if num <= 1:
    fib = num
else:
    fib = 0
    one_back = 1
    two_back = 0
    print("0, 1, ", end="")
    for i in range(2, num + 1):
        fib = one_back + two_back
        two_back = one_back
        one_back = fib
        print(fib, end=", ")
print('\n' + str(fib))

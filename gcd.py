# gcd(a, b) = gcd(a', b) = gcd(b, a')


def gcd(a, b):
    # once b = 0, a will be the GCD
    if b == 0:
        return a
    aprime = a % b
    # now return recursively, passing b for a and a' for b
    # print(f"({a}, {b})")  # not necessary, only included to see what happens
    return gcd(b, aprime)


def lcm(a, b):
    return abs(a * b) / gcd(a, b)


print(gcd(1344, 217))
print(217 / 42)
print()
print(lcm(15, 3))
print()
num1 = 28851538
num2 = 1183019
least = 1933053046
# print(lcm(num1, num2))
print(gcd(num1, num2))
print(lcm(num1, num2))
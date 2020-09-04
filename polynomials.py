def multipoly(a, b, n):
    product = []
    for i in range(0, (2 * n - 2) + 1):
        product.append(0)
    for i in range(0, (n - 1) + 1):
        for j in range(0, (n - 1) + 1):
            product[i + j] = product[i + j] + (a[i] * b[j])
    return product


A = [3, 2, 5]
B = [5, 1, 2]
print(multipoly(A, B, 3))

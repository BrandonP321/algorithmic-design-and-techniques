def unit_value(arr):
    unitValues = []
    for item, weight, value in arr:
        unitValues.append((value / weight, item, weight))
    return sorted(unitValues, reverse=True)


def sack(w, arr):
    unit_values = unit_value(arr)
    amounts = []
    total_weight = 0
    total_value = 0
    for unit_price, item, weight in unit_values:
        if w - total_weight <= weight:
            weight_add = w - total_weight
            total_value += weight_add * unit_price
            amounts.append((item, f"{weight_add}g", f"${unit_price * weight_add}"))
            break
        else:
            total_value += unit_price * weight
            total_weight += weight
            amounts.append((item, f"{weight}g", f"${unit_price * weight}"))
    return total_value, amounts


mylist = [('oats', 5, 30), ('cereal', 4, 28), ('rice', 3, 24)]
mylist = [('one', 20, 20), ('two', 5, 10), ('three', 4, 20)]
my_sack = sack(10, mylist)
print(my_sack)

for item, weight, value in my_sack[1]:
    print(item, weight, value)


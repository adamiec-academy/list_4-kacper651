import math


def min_max(data):
    min_val = math.inf
    max_val = -math.inf
    for digit in data:
        if digit < min_val:
            min_val = digit
    for digit in data:
        if digit > max_val:
            max_val = digit

    return min_val, max_val


list1 = [-5, 3, 3, 7, 12, -2, 0, 12, 1]

print(min_max(list1))

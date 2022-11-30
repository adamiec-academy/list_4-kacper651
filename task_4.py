def info(data):
    for row in data:
        for element in row:
            print(element, end="")
        print()


def border_map(a, b):
    matrix = []
    for i in range(b):
        matrix.append([])
        for j in range(a):
            if i == 0 or j == 0 or i == b-1 or j == a-1:
                matrix[i].append('X')
            else:
                matrix[i].append('.')

    return matrix


print(border_map(15, 8))
print()
info(border_map(15, 8))

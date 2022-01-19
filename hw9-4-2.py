# Nolan Piselli

def products(number, val_2):
    for index, value in enumerate(number):
        number[index] = value * val_2
        value *= val_2
    return number
print(products([3, 4], 3))
single_digits = range(10)
squares = []
for i in single_digits:
    print(i)
    squares.append(i**2)
    

cubes = [num ** 3 for num in single_digits]
print(cubes)
# Python automatically type casts y into float
y = 7 + 2.2

# Output: 9.2
print(y)

# Output: <class 'float'>
print(type(y))


# input: to let the user interact by adding a string value.
# Wrong conde: num = input("Please enter a number: ")
# To make it work:
num = int(input("Please enter a number: "))
print(num ** 2)
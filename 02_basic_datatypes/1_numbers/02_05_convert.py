'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
# 1) Convert an int to a float
i2f = 2
print(type(i2f))
i2f = float(i2f)
print(type(i2f))
# 2) Convert a float to an int
f2i = 2.5
print(type(f2i))
f2i = int(f2i)
print(type(f2i))
# 3) Perform floor division using a float and an int.
print("in floor division, 3 / 2.1 =", 3 // 2.1)
# 4) Use two user inputted values to perform multiplication.
num1 = float(input("Enter the first number you want to multiply: "))
num2 = float(input("Enter the second number you want to multiply: "))
print(num1, "x", num2, "=", num1*num2)

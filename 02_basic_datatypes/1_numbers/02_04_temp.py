'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

degF = float(input("Enter the temperature in degrees Fahrenheit: "))
print(degF, "degrees Fahrenheit =", (degF - 32) * (5 / 9), "degrees Celsius")

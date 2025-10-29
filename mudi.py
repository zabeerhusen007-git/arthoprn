# Simple Python program for multiplication and division of two numbers

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Multiplication
multiplication = num1 * num2

# Division (checking for division by zero)
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)"

# Displaying the results
print(f"The result of multiplication is: {multiplication}")
print(f"The result of division is: {division}")

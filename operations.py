# Program to perform addition, subtraction,
# multiplication and division of two numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
addition = num1 + num2

# Subtraction
subtraction = num1 - num2

# Multiplication
multiplication = num1 * num2

# Division
if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

# Display results
print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
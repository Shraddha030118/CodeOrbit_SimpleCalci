# Simple Calculator

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Asking the user to choose an operation
operation = input("Enter operation (+, -, *, /): ")

try:
    # Performing the selected operation
    if operation == "+":
        result = num1 + num2

    elif operation == "-":
        result = num1 - num2

    elif operation == "*":
        result = num1 * num2

    elif operation == "/":
        result = num1 / num2

    else:
        print("Invalid operation!")
        result = None

    # Displaying the result
    if result is not None:
        print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")
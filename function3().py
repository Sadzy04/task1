
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed"

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Error: Division by zero is not allowed"

def exponent(x, y):
    return x ** y


x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /, %, **): ")

if operation == "+":
    print(f"The result is: {add(x, y)}")
elif operation == "-":
    print(f"The result is: {subtract(x, y)}")
elif operation == "*":
    print(f"The result is: {multiply(x, y)}")
elif operation == "/":
    print(f"The result is: {divide(x, y)}")
elif operation == "%":
    print(f"The result is: {modulus(x, y)}")
elif operation == "**":
    print(f"The result is: {exponent(x, y)}")
else:
    print("Error: Invalid operation")

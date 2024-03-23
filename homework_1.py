# Calculator App

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

def calculator():
    a = int(input("Welcome to the calculator app. Press enter first value: "))
    b = int(input("Enter second value: "))
    
    operation = input("Enter the operation you would like to perform: +, -, *, /")
    
    if operation == "+":
        print(add(a, b))
    elif operation == "-":
        print(subtract(a, b))
    elif operation == "*":
        print(multiply(a, b))
    elif operation == "/":
        print(divide(a, b))
    else:
        print("Invalid operation")        

calculator()
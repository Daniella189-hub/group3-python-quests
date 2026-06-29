def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b== o:
        return "Error cannot divide by zero"
    return a / b
num1 = float(input("enterfirst number: "))
num2 = float(input("enter second number: "))
operation = input("enter operation (add, subtract, multiply, divide): ")
if operation == "add":
    print(f"The result is: {add(num1,num2)}")
elif operation == "subtract":
    print(f"The result is: {subtract(num1,num2)}")
elif operation == "multiply":
    print(f"The result is: {multiply(num1,num2)}")
elif operation == "divide":
    print(f"The result is: {divide(num1,num2)}")
else:
    print("Wrong operation.")    
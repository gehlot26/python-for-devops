#Simple Calculator Program

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero!"
    

num1 = 10 
num2 = 5

print("Addition : ", add(num1, num2))
print("Subtraction : ", sub(num1, num2))
print("Multiplication: ", multiply(num1, num2))
print("Division: ", divide(num1, num2))
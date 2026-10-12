def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x /y

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("sum of two numbers is: ", add(num1, num2))
print("difference of two numbers is: ", subtract(num1, num2))
print("product of two numbers is: ", multiply(num1, num2))
print("quotient of two numbers is: ", divide(num1, num2))
from art import logo
print(logo)

def add(n1,n2):
    return n1 + n1

def subtrack (n1,n2):
    return n1 - n2

def miltuply (n1,n2):
    return n1 * n2

def divide (n1,n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Dividing by zero, not alloved"

operations = {
    '/':divide,
    '+':add,
    '-':subtrack,
    '*':miltuply,
    }

num1 = int(input("Enter the first number: "))

for operation in operations:
    print(operation)
operation_symbol = input("Pick the operation  from above: ")
num2 = int(input("Enter the second number: "))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
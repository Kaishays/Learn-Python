def calculator():
    #get integer input 
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    #int - str to num converter 
    #float - decimal number 
    result = int(num1) + float(num2)
    return result
    

def calculator_better():
    #get input convert to float
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter another number: "))
    #use if statement to define operator 
    op = input("Enter operator: ")
    #do caclulation 
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else: 
        print("Invalid operator")

calculator_better()
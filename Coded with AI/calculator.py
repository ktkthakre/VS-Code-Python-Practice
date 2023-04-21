"""
-welcome user
-print list of operations to perform and ask user for input
-function to create a calculator that can perform following operations:
addition
subtraction
multiplication
division
square root
-function will take two numbers as input and ask user which operation to perform
-asks user if they want to exit, if yes then closes the program
-ask user after  each operation to continue or exit
"""

def welcome():
    print("Welcome to the calculator")
    print("Here are the operations you can perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square root")
    print("6. Exit")
    print("Enter the number corresponding to the operation you want to perform")
    return
    
def operation():
    operation = int(input())
    if operation == 1:
        print("Enter the first number")
        num1 = int(input())
        print("Enter the second number")
        num2 = int(input())
        print("The sum of the two numbers is", num1 + num2)
    elif operation == 2:
        print("Enter the first number")
        num1 = int(input())
        print("Enter the second number")
        num2 = int(input())
        print("The difference of the two numbers is", num1 - num2)
    elif operation == 3:
        print("Enter the first number")
        num1 = int(input())
        print("Enter the second number")
        num2 = int(input())
        print("The product of the two numbers is", num1 * num2)
    elif operation == 4:
        print("Enter the first number")
        num1 = int(input())
        print("Enter the second number")
        num2 = int(input())
        print("The quotient of the two numbers is", num1 / num2)
        print("The remainder of the two numbers is", num1 % num2)
    elif operation == 5:
        print("Enter the number")
        num1 = int(input())
        print("The square root of the number is", num1 ** 0.5)
        
    else:
        print("Exiting the program")
        exit()
    
    print("Do you want to perform another operation?")
    print("1. Yes")
    print("2. No")
    choice = input()
    if choice == '1' or choice == 'Yes' or choice == 'yes':
        operation()
    else:
        print("Exiting the program")
        exit()
        
welcome()
operation()
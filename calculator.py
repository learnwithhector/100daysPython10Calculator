import sys, os
from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    os.system('cls')
    print(logo)
    result = 0
    num1 = float(input("What's the first number? "))
    while True:
        print("Pick an operation")
        for key, _ in operations.items():
            print(key)
        operation_symbol = input()
        num2 = float(input("What's the next number? "))
        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        num1 = result
        again = input(f"Type 'y' to keep calculating with {result} 'q' to quit or anything else to "
                      f"start a new calculation: ").casefold()
        if again == 'q' or again == 'quit':
            print("You quit")
            sys.exit()
        elif again != 'y' and again != 'yes':
            calculator()
        else:
            continue


calculator()

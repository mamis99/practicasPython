import os
import time

def add(x,y):
    return x + y
def substract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        return 'Infinite'
    else:
        return x / y

operations_dictionary = {'+':add,
                         '-':substract,
                         '*':multiply,
                         '/':divide
                         }

symbol_list = ['+', '-', '*', '/']

for _ in range(0,3):
    symbol = input('select an operation from the dictionary: ')

    if symbol in symbol_list:
        calculation_function = operations_dictionary[symbol]

        x = int(input('Type a number: '))
        y = int(input('Type another number: '))

        result = calculation_function(x,y)
        print(result)

    if not symbol in symbol_list:
        print('There isn´t a symbol operation')

    time.sleep(3)
    os.system('clear')
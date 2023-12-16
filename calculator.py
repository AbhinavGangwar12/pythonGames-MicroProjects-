import math
import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def multiply(num1,num2):
    return num1*num2

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def div(num1,num2):
    return num1/num2

def mod(num1,num2):
    return num1%num2

def power(num1,num2):
    return pow(num1,num2)

operations = {
    "*" : multiply,
    "+" : add,
    "-" : sub,
    "/" : div,
    "%" : mod,
    "**" : power,
}



loop = True
while loop:
    print(logo)
    num1 = int(input("Enter number : "))
    num2 = int(input("Enter number : "))
    print("Which opereations you want to perform")
    for op in operations:
        print(op)
    ops = input(">>")
    function = operations[ops]
    print(f"{num1} {ops} {num2} = {function(num1,num2)}")
    i = input("Enter 'yes' to use again otherwise enter 'no' : ").lower()
    if i == "no":
        loop = False
    else:
        os.system('cls')
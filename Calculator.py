import time


def add(num1, num2):
    """Returns num1 plus num2"""
    return num1 + num2


def sub(num1, num2):
    """Returns num1 minus num2"""
    return num1 - num2


def mul(num1, num2):
    """Returns num1 times num2"""
    return num1 * num2


def div(num1, num2):
    """Returns num1 divided by num2"""
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Handled Div By Zero. Returning Zero")
        return 0


def runOperation(operation, num1, num2):
    """Determines the operation to run based on the
    operation argument which should be passed in as an int"""
    # Determine operation
    if operation == 1 or operation == '+':
        print("Adding Numbers...")
        time.sleep(1)
        print(add(num1, num2))

    elif operation == 2 or operation == '-':
        print("Subtracting Numbers...")
        time.sleep(1)
        print(sub(num1, num2))

    elif operation == 3 or operation == '*':
        print("Multiplying Numbers...")
        time.sleep(1)
        print(mul(num1, num2))

    elif operation == 4 or operation == '/':
        print("Dividing Numbers...")
        time.sleep(1)
        print(div(num1, num2))

    else:
        print("Retry")


def result():
    """Allows User To Run Basic Calculator Operations With Two Numbers."""
    valiant = False
    while not valiant:
        # Get user input
        try:
            num1 = int(input("Enter Number 1 : "))
            num2 = int(input("Enter Number 2 : "))
            ooperation = int(input('What Do You Want To Do ? 1. Add, 2. Subtract, 3. Multiply Or 4. Divide.'
                                  'Enter Number: '))
            valiant = True
        except ValueError:
            print("Invalid Input. Please Try Again... ")
        except:
            print("Unknown Error")
        runOperation(ooperation, num1, num2)


result()


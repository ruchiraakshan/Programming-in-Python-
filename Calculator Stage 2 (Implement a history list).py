# List to store history
history_list = []

# Arithmetic operation functions
def add(a,b):
    return a+b
  
def subtract(a,b):
    return a-b
  
def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        return a/b
    except Exception as e:
        print(e)  # prints 'float division by zero'
        return None

def power(a,b):
    return a**b
  
def remainder(a,b):
    try:
        return a % b
    except Exception as e:
        print(e)
        return None

# Function to handle history
def history():
    if not history_list:
        print("No past calculations to show")
    else:
        for item in history_list:
            print(item)

# Function to select operation
def select_op(choice):
    if choice == '#':
        return -1
    elif choice == '$':
        return 0
    elif choice == '?':
        history()
        return 0
    elif choice in ('+','-','*','/','^','%'):
        # Get first number
        while True:
            num1s = str(input("Enter first number: "))
            print(num1s)
            if num1s.endswith('$'):
                return 0
            if num1s.endswith('#'):
                return -1
            try:
                num1 = float(num1s)
                break
            except:
                print("Not a valid number,please enter again")
                continue
        
        # Get second number
        while True:
            num2s = str(input("Enter second number: "))
            print(num2s)
            if num2s.endswith('$'):
                return 0
            if num2s.endswith('#'):
                return -1
            try:
                num2 = float(num2s)
                break
            except:
                print("Not a valid number,please enter again")
                continue
        
        # Perform calculation
        result = None
        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)
        elif choice == '^':
            result = power(num1, num2)
        elif choice == '%':
            result = remainder(num1, num2)
        else:
            print("Something Went Wrong")
        
        # Save to history
        last_calculation = "{0} {1} {2} = {3}".format(num1, choice, num2, result)
        print(last_calculation)
        history_list.append(last_calculation)
    else:
        print("Unrecognized operation")
    return 0

# Main loop
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ? ")
    
    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)
    if select_op(choice) == -1:
        print("Done. Terminating")
        exit()

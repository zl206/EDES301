

#python2 reads "raw_input()" as a string and reads "input()" as code
#python3 reads "input()" as a string and does not have "raw_input()" function
try:
    # if using python2, then this ensures the function reads the input as a string 
    input = raw_input
except NameError:
    #if using python3 then don't change anything
    pass

def right_shift(a, b):
    return int(a) >> int(b)

def left_shift(a, b):
    return int(a) >> int(b)

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    ">>": right_shift,
    "<<": left_shift,
    "%": operator.mod,
    "**": operator.pow
}

def get_user_input():
    try:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        op = input("Enter function (valid values are +, -, *, /, >>, <<, %, **): ")
        
        func = operators.get(op)
    except:
        return (None, None, None)
        
    return (number1, number2, func)
    
    
if __name__ == "__main__":
    while True:
    
        (num1, num2, func) = get_user_input()
        
        if (num1==None) or (num2==None) or (func==None):
            print("Invalid input")
            break
        
        print(func(num1,num2))
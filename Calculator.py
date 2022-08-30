#Calculator Functionality
import math

print("""
Press 1 for Addition
Press 2 for Subtraction
Press 3 for Multiplication
Press 4 for Division
Press 5 for Modulus
Press 6 for Square
Press 7 for Square Root
Press 8 for Power
Press 9 to Quit
    """)
try:
    operator = int(input("Enter the operation : "))
except ValueError:
    print("ValueError")
if operator == 1 :
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    temp = a + b
    word = "Addition"
    print(f"The resultant after {word.lower()} of number(s) is {temp}")
elif operator == 2 :
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    temp = a - b
    word = "Subtraction"
    print(f"The resultant after {word.lower()} of number(s) is {temp}")
elif operator == 3 :
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    temp = a * b
    word = "Multiplication"
    print(f"The resultant after {word.lower()} of number(s) is {temp}")
elif operator == 4 :
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    if b == 0:
        print("Divide by 0 Error")
    else :
        temp = a / b
        word = "Division"
        print(f"The resultant after {word.lower()} of number(s) is {temp}")
elif operator == 5 :
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    temp = a % b
    word = "Modulus"
    print(f"The resultant after {word.lower()} of number(s) is {temp}")
elif operator == 6 :
    a = float(input("Enter the first number : "))
    temp = a ** 2
    word = "Square"
    print(f"The resultant after {word.lower()} of number is {temp}")
elif operator == 7 :
    a = float(input("Enter the first number : "))
    temp = math.sqrt(a)
    word = "Square Root"
    print(f"The resultant after {word.lower()} of number is {temp}")
elif operator == 8 :
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    temp = a ** b
    word = "Power"
    print(f"The resultant after {word.lower()} of number(s) is {temp}")
elif operator == 9 :
    print("GoodBye")
else :
    print("You have entered an invalid operation\nGoodbye")

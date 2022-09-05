import logging
logging.basicConfig(filename="Calc.log",level=logging.DEBUG,format="%(name)s %(asctime)s %(levelname)s %(message)s")

import math
print ("*****CALCULATOR******")

class Calculator:
    def add(self,a,b):
        return a + b
    def sub(self,a,b):
        return a - b
    def mul(self,a,b):
        return a * b
    def div(self,a,b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Number cannot be divided by 0")
    def mod(self,a,b):
        return a % b
    def sq(self,a):
        return a ** 2
    def sqrt(self,a):
        return math.sqrt(a)
    def pow(self,a,b):
        return a ** b

a = int(input("Please enter the number: "))
x = int(input("""Please enter the operation to be performed on said number:
Press 1 for Addition
Press 2 for Subtraction
Press 3 for Multiplication
Press 4 for Division
Press 5 for Modulus
Press 6 for Square
Press 7 for Square Root
Press 8 for Power
Press 9 to Quit
"""))

var = Calculator()
if x ==6:
    print(var.sq(a))
    logging.info(f"The user wants to perform square operation on {a}")
elif x ==7:
    print(var.sqrt(a))
    logging.info(f"The user wants to perform square root of {a}")
elif x ==9:
    print("Goodbye")
else :
    b = int(input("Enter the second operand: "))
    if x ==1:
        y = "Addition"
        print(var.add(a,b))
    if x ==2:
        print(var.sub(a,b))
        y = "Subtraction"
    if x ==3:
        print(var.mul(a,b))
        y = "Multiplication"
    if x ==4:
        print(var.div(a,b))
        y = "Divide"
    if x ==5:
        print(var.mod(a,b))
        y = "Modulus"
    if x ==8:
        print(var.pow(a,b))
        y ="Exponentiation"
    logging.info(f"The user wants to perform {y.lower()} operation on {a} and {b}")
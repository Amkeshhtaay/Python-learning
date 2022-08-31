l = []
number = int(input("Please enter the number of values required : "))
for i in range(number) :
    a = int(input(f"Please enter the {i+1} value : "))
    l.append(a)
print('The list prepared by using values provided by you is : ',l)

#For specified number of rotations
"""b = int(input("Please enter number of rotations : "))
for i in range(b) :
    c = l.pop()
    l2 = l
    l2.insert(0,c)
    print(l2)"""

#For complete rotation
for i in range(len(l)):
    a = l.pop()
    l1 = l
    l1.insert(0,a)
    print(l1)
print(i+1)
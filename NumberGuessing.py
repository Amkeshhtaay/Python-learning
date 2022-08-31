import random
print("Select the range of numbers you have to guess within")
a = int(input("Please enter the smallest number : "))
b = int(input("Please enter the largest number : "))

c = random.randint(a,b)

attempt = 0
guess = 0
while guess!= c:
    guess = int(input("Please enter your guess number : "))
    if guess == c:
        print(f"Woohoo!! You got the correct guess in {round(attempt/2)+1} attempts")
    if guess > c :
        print("Please enter a smaller number")
        attempt+= 1
        if abs(c-a) < abs(c-b):
            b = round((a+b)/2)
            print(f"Values lie between {a} and {b}")
            attempt+= 1
        elif abs(c-a) > abs(c-b):
            a = round((a+b)/2)
            print(f"Values lie between {a} and {b}")
            attempt+= 1
        elif abs(c-a) == abs(c-b):
            a = a+1
            b = b-1
            print(f"Values lie between {a} and {b}")
            attempt+= 1
    elif guess < c :
        print("Please enter a greater number")
        attempt+= 1
        if abs(c-a) > abs(c-b):
            a = round((a+b)/2)
            print(f"Values lie between {a} and {b}")
            attempt+= 1
        elif abs(c-a) < abs(c-b):
            b = round((a+b)/2)
            print(f"Values lie between {a} and {b}")
            attempt+= 1
        elif abs(c-a) == abs(c-b):
            a = a+1
            b = b-1
            print(f"Values lie between {a} and {b}")
            attempt+= 1




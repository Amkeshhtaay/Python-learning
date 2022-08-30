import random

lucky_number = random.randint(1,100)

fortune_number = random.randint(1,6)

if fortune_number == 1 :
    fortune_text = "A smart and loving person will be coming into your life!"
elif fortune_number == 2 :
    fortune_text = "A dubious friend may be an enemy in camouflage!"
elif fortune_number == 3 :
    fortune_text = "Adventure can be real happiness!"
elif fortune_number == 4 :
    fortune_text = "All will go well with your next project!"
elif fortune_number == 5 :
    fortune_text = "Don't just think, Act!"
elif fortune_number == 6 :
    fortune_text = "It takes courage to admit fault!"

print(f"{fortune_text} Your lucky number is {lucky_number}")
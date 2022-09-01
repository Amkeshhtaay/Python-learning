#To check if given text is a palindrome or not
import string
def is_palindrome(a):
    a=a.lower().replace(' ','')
    a = a.replace(string.punctuation, '')
    a = a.replace('.', '')
    x=0
    y=1
    for x in range(len(a)):
        if((a[x] == a[len(a)-x-1])):
            return True
        if ((a[x] != a[len(a)-x-1])):
            return False

print(is_palindrome("""Go hang a salami - I'm a lasagna hog."""))


#    elif i >0:
#        print(a[y],a[len(a)-y-1] )
#        y += 1
#        print("The given string is a palindrome")
#    else :
#        print("The string is not a palindrome")

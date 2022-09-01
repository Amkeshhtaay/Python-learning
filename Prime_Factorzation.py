def all_factors(a):
    l1 = []
#    a = int(input("Please enter the number for which all factors are required: "))
    for i in range(1,a):
        if a % i == 0:
            l1.append(i)
    l1.append(a)
    return l1

def prime_Factorization(b):
#    b = int(input("Please enter the number for which prime factors are required: "))
    l = []
    divisor = 2
    while (divisor <= b):
        if b % divisor == 0:
            l.append(divisor)
            b = b / divisor
        else :
            divisor += 1
    return l

print(prime_Factorization(60))
print(all_factors(60))
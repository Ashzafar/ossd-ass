# F2020266454
def is_prime(number):
    divisor = number - 1
    flag=True
    while divisor > 1:
        if number % divisor == 0:
            flag=False
        divisor = divisor - 1
    print("is prime" if flag==True else "not prime")

is_prime(4)

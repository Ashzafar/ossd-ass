# F2020266454
def factorial(number, sum=1):
    if number == 0:
        return sum
    else:
        sum = sum * number
        return factorial(number - 1, sum)


print(factorial(5))

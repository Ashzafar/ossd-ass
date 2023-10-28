# F2020266454
def sum_of_digits(number,sum=0):
    if number//10<1:
        return sum+number
    else:
        return sum_of_digits(number//10,sum+number%10)    
print(sum_of_digits(73))
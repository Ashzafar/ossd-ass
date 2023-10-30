# written by Ashir Mehmood

num = int(input("Enter number: "))

def fib(num: int) -> int:
    if num == 0:
        return 0
    
    elif num == 1:
        return 1

    else:
        return fib(num - 1) + fib(num - 2)


print(fib(num))

# other way


def fib2(num: int) -> int:
    a, b = 0 ,1
    result = []
    for i in range(num):
        result.append(a)
        a, b = b, a + b
    return result    


print(fib2(num))   
            
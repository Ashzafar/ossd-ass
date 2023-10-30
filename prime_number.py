# written by Ashir Mehmood

num = int(input("enter num to check prime, if it is or not: "))


def is_prime(num, i):

    if num == 0 or num == 1:
        return False

    if num == i:
        return True

    if (num % i == 0):
        return False

    i += 1
    return is_prime(num, i)


def __main__():
    if(is_prime(15,2)):
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    __main__()

def gcd(x: int, y: int) -> int:
    if x>y:
        temp = x
    else:
        temp = y

    for i in range(1, temp+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd

num_x = int(input("x: "))
num_y = int(input("y: "))

print(gcd(num_x, num_y))

def lcm(x: int, y: int)-> int:

    lcm = []

    if x>y:
        temp = x
    else:
        temp = y

    for i in range(1, temp+1):
        if((x % i == 0) and (y % i == 0)):
            lcm.append(i)

    lcm.sort()

    return lcm[1]

num_x = int(input("x: "))
num_y = int(input("y: "))

print(lcm(num_x, num_y))
# password generator script

import random

length = int(input("Enter the password's length "))
while length <=10:
    key = "1256yuiiopa789()$#xcvb@#!qwert34sdfg*&^%hjklznm"
    generated_password = "".join(random.sample(key, length))
    print(generated_password)
    break

exit()

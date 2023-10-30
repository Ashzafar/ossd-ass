# written by Ashir Mehmood'




def is_pal(str):
    flag = 1
    lenght = len(str)
    reverse_iter = lenght-1
    i = 0

    while(reverse_iter >= 0):
        if str[reverse_iter] == str[i]:
            reverse_iter -= 1
            i += 1
            flag = 1
        else:
            flag = 0
            break

    return flag            

user_input = input("enter string: ")

if is_pal(user_input) == 1:
    print("palindrome")
else:
    print("not a palindrome")
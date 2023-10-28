# F2020266454

def reverse_string(string):
    i=len(string)-1
    reversed=[]
    while i >=0:
        reversed.append(string[i])
        i-=1
    print(''.join(reversed))
reverse_string('join')
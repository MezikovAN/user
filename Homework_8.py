first = int(input('First :'))
second = int(input('Second :'))
third = int(input('Third :'))
# первое условие
if first == second == third:
    print (3)
# второе условие
elif first == second or first == third or second == third:
    print (2)
else :
    print (0)
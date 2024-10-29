n = int(input('ведите число от 3 до 20 :'))
if n <= 20 and n >=3:
    p = ''
    for i in range(1,21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                p = str(i) + str(j)
print (p)

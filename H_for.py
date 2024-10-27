numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []      # Список для простых чисел
not_primes = []  # Список для составных чисел

for number in numbers:
    if number > 1:  # Число должно быть больше 1, чтобы быть простым
        is_prime = True
        for i in range(2, number):
            if (number % i) == 0:
                is_prime = False
                not_primes.append(number)
                break
        if is_prime:
            primes.append(number)
    else:
        not_primes.append(number)

print("Primes:", primes)
print("Not Primes:", not_primes)

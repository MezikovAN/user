def get_multiplied_digits(number):
    # Преобразуем число в строку для удобного обращения к цифрам
    str_number = str(number)

    # Извлекаем первую цифру и преобразуем её в int
    first = int(str_number[0])

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если осталась только одна цифра, возвращаем её
        return first
result = get_multiplied_digits(40203)

print(result)
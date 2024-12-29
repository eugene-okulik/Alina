import sys


def f_numbers(limit):
    numbers = [0, 1]
    yield numbers[0]
    yield numbers[1]
    i = 0
    while i <= limit:
        a = numbers[-1]
        b = numbers[-2]
        c = a + b
        numbers.append(c)
        yield c
        i += 1


for n, num in enumerate(f_numbers(100001)):
    if n == 5:
        print("Пятое:", num)
    elif n == 200:
        print("Двухсотое:", num)
    elif n == 1000:
        print("Тысячное:", num)
    elif n == 100000:
        sys.set_int_max_str_digits(n)
        print("Cтотысячное:", num)
        break

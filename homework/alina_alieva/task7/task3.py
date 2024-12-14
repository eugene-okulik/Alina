String_one = "результат операции: 42"
String_two = "результат операции: 54"
String_three = "результат работы программы: 209"
String_four = "результат: 2"


def find_number(string):
    mass = string.split(':')
    result = int(mass[1]) + 10
    print(result)


arr = [String_one, String_two, String_three, String_four]
for pair in arr:
    find_number(pair)

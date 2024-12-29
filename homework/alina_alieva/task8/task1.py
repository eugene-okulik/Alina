import random


def random_bonus():
    numb = random.randint(1, 100)
    yield numb


def bool_for_bonus():
    a = [True, False]
    bonus_bool = random.choice(a)
    yield bonus_bool


while True:
    salary = input("Please input your salary ")
    bool_bonus = next(bool_for_bonus())
    bonus = next(random_bonus())
    if salary == 'break':
        print("The end")
        break
    if bool_bonus:
        result = int(salary) + bonus
        print(f"{bonus}, {bool_bonus} - '${result}'")
    else:
        print("False")

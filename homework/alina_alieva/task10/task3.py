def operator(func):
    def wrapper(first1, second1):
        if first1 < 0 or second1 < 0:
            operation = '*'
        elif first1 == second1:
            operation = '+'
        elif first1 > second1:
            operation = '-'
        elif second1 > first1:
            operation = '/'
        return func(first1, second1, operation)
    return wrapper


@operator
def calc(first1, second1, operation):
    if operation == '+':
        return first1 + second1
    elif operation == '-':
        return second1 - first1
    elif operation == '/':
        return first1 / second1
    elif operation == '*':
        return first1 * second1
    else:
        return "Unknown operation"


first2 = int(input("Input First number "))
second2 = int(input("Input Second number "))
result = calc(first2, second2)
print(result)

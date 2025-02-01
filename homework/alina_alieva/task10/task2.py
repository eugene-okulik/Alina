def repeat_me(**kwargs):
    def number(func):
        def wrapper(*args):
            count = kwargs.get('count')
            for _ in range(count):
                func(*args)
        return wrapper
    return number


@repeat_me(count=5)
def example(text):
    print(text)


example('print me')

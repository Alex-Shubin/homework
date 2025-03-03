"""
Написать функцию hello, которая принимает 2 аргумента name и surname и
выводит принтом "Привет, {name} {surname}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
Выполняеся функция <имя> с аргументами <аргументы> 
После выполнения функции напечатать строку "<имя функции> - завершена"
"""
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняется функция {func.__name__}"
              f"с аргументами {kwargs.get('name')}, {kwargs.get('surname')}")
        func(*args, **kwargs)
        print(f"{func.__name__} - завершена")

    return wrapper

@log_decorator
def f_hello(name, surname):
    print(f"Привет, {name} {surname}")
    return

f_hello(name="Denis", surname="Pupkin")
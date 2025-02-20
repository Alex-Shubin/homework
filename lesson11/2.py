"""
Написать функцию hello, которая принимает 2 аргумента name и surname и
выводит принтом "Привет, {name} {surname}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
Выполняеся функция <имя> с аргументами <аргументы> 
После выполнения функции напечатать строку "<имя функции> - завершена"
"""
def log_decorator(func):
    def wrapper(name, surname):
        print(f"Выполняется функция {func.__name__} с аргументами {name}, {surname}")
        result = func(name, surname)
        print(f"{func.__name__} - завершена")
        return result
    return wrapper

@log_decorator
def f_hello(name, surname):
    print(f"Привет, {name} {surname}")
    return

f_hello(name="Denis", surname="Pupkin")
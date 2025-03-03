"""
Написать декоратор который позволит не останавливать программу 
в случае если любая декорируемая функция выбрасывает ошибку, 
а выводить имя функции в которой произошла ошибка и информацию об ошибке в. 
Имя функции можно узнать использовав свойство __name__ ( print(func.__name__))

* сделать настраиваемы параметр который определяет печать в консоль или в файл
и если в файл передать название фала
"""

def error_wrapper(func):
    """
    Декоратор, который не останавливает программу в случае ошибки,
    а возвращает текст ошибки с названием функции и самим текстом ошибки.
    Используется func.__name__

    Необязательный параметр filename - имя файла
    """
    def wrapper(*args, filename = None, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as error:
            result = f"Ошибка в {func.__name__}: {error}"
        if filename:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(str(result)+"\n")
                return result   
        else:
            return result
        
    return wrapper
    
@error_wrapper
def f1(x, y):
    return x / y

@error_wrapper
def f2(a, b):
    return a + b + c # c не определена

# result1 = f1(6, 3, filename="lesson11\\234.txt")
# print(result1) # будет 2.0 - запишет в файл 123.txt в корне и 
print(f1(6, 3))

result2 = f1(6, 0, filename="lesson11\\234.txt")
print(result2) # будет ошибка деления на 0

result3 = f2(3, 5, filename="lesson11\\234.txt")
print(result3) # будет ошибка - нет переменной
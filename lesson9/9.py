"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").

Если все именованные аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""
def dict_from_args(*args, **kwargs):
    try:
        if all(isinstance(x, int) for x in args):
            args_sum = sum(list(args))
        else:
            raise TypeError("Все позиционные аргументы должны быть целыми")
    except TypeError as e:
        print(f"Все позиционные аргументы должны быть целыми")
    try:
        if all(isinstance(x, str) for x in kwargs.values()):
            kwargs_len = list()
            for kwarg in kwargs.values():
                kwargs_len.append(len(kwarg))
            kwargs_max_len = max(kwargs_len)
        else:
            raise TypeError("Все аргументы - ключевые слова должны быть строками")
    except TypeError as e:
        print(f"Все аргументы - ключевые слова должны быть строками")
    return {"args_sum": args_sum if 'args_sum' in locals() else None,
            "kwargs_max_len": kwargs_max_len if 'kwargs_max_len' in locals() else None}

print(dict_from_args(1,2,3,4,5,6,7,8,9,key1="1",key2="awdsads",key3="wdwdsd"))
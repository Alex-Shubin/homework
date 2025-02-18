"""
Написать генератор последовательности Фибоначчи, 
который принимает максимальное количество чисел в последовательности 
из чисел Фибоначчи и генерирует последовательность. 
Затем  вывести на экран элементы данного генератора. 
Фибоначчи последовательность - первые два числа которой являются 0 и 1, 
а каждое последующее за ними число является суммой двух предыдущих. 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 и так далее.  
"""
def fibo_gen(max_num):
    a, b = 0, 1
    index = 0

    while index < max_num:
        yield a
        a, b = b, a + b
        index += 1

result = fibo_gen(10)
for num in result:
    print(num)
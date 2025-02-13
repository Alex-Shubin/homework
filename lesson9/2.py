'''
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.

'''

def factorial(num):
    if num == 1:
        return 1
    return factorial(num - 1) * num

print(factorial(5))
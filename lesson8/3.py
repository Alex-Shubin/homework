'''
Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.

'''
def factorial(user_input:int):
    fact = 1
    for i in range(2, user_input+1):
        fact *= i
    return fact

# user_number = int(input("Введите число: "))
# print(factorial(user_number))
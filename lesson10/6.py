"""
Написать генератор triangular_numbers, который возвращает подряд 
треугольные числа

Формула:
Tn = 1 / 2 * n * (n + 1)

Например:
tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21
"""
def triangular_numbers(max_n:int):
    n = 1
    while n <= max_n:
        tn = 1 / 2 * n * (n + 1)
        yield int(tn)
        n += 1

tn_gen = triangular_numbers(5)

for num in tn_gen:
    print(num)
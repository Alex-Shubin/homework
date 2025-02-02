'''
Запросить 3 раза строку из нескольких чисел через пробел
    - вывести все уникальные числа по возрастанию
    - вывести числа которые есть в каждой строке
    -* вывести числа которые есть только в одной из трех строк
    
    выполнить без циклов и условий
    
    пример:
    >>> 1 2 11 22
    >>> 1 2 22 33
    >>> 1 2 33 44


    1) 1 2 11 22 33 44
    2) 1 2
    3) 11 44
    
'''
user_set1 = set(list(map(int, input("Введите несколько чисел через пробел: ").split())))
user_set2 = set(list(map(int, input("Введите несколько чисел через пробел: ").split())))
user_set3 = set(list(map(int, input("Введите несколько чисел через пробел: ").split())))

# user_set1 = set(list(map(int, "1 2 11 22".split())))
# user_set2 = set(list(map(int, "1 2 22 33".split())))
# user_set3 = set(list(map(int, "1 2 33 44".split())))

print(sorted(list(user_set1.union(user_set2, user_set3))))
print(list(user_set1.intersection(user_set2, user_set3)))

user_list = list(user_set1)
user_list.extend(list(user_set2))
user_list.extend(list(user_set3))

print("Метод 1: ", *filter(lambda x: user_list.count(x) == 1, user_list))

from collections import Counter
c = Counter()
c = Counter(user_list)
# print(c)

# sorted(c.elements(), reverse=True) # не нужен
print("Метод 2: ", *filter(lambda x: c.get(x) == 1, c))

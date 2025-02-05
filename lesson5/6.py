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
# user_set1 = set(list(map(int, input("Введите несколько чисел через пробел: ").split())))
# user_set2 = set(list(map(int, input("Введите несколько чисел через пробел: ").split())))
# user_set3 = set(list(map(int, input("Введите несколько чисел через пробел: ").split())))

user_set1 = set(list(map(int, "1 2 11 22".split())))
user_set2 = set(list(map(int, "1 2 22 33".split())))
user_set3 = set(list(map(int, "1 2 33 44".split())))

print("все уникальные числа по возрастанию", sorted(list(user_set1.union(user_set2, user_set3))))
print("числа которые есть в каждой строке", list(user_set1.intersection(user_set2, user_set3)))

# как-то громоздко получилось...

user_set = user_set1.copy()
user_set.update(user_set2, user_set3) # сделал копию всех чисел в множестве
# print(user_set) 

user_set_cut1 = user_set1.intersection(user_set2) # общее между 1 и 2
user_set_cut2 = user_set2.intersection(user_set3) # общее между 2 и 3
user_set_cut3 = user_set1.intersection(user_set3) # общее между 1 и 3

# print(user_set_cut1, user_set_cut2, user_set_cut3) 

user_set_cut1.update(user_set_cut2, user_set_cut3) # сделал множество только повторяющихся значений

# print(user_set_cut1)

print("-* вывести числа которые есть только в одной из трех строк: ", 
      user_set.difference(user_set_cut1))

# решения через условие

user_list = list(user_set1)
user_list.extend(list(user_set2))
user_list.extend(list(user_set3))

print("Метод 2 с условием - .count: ", 
      *filter(lambda x: user_list.count(x) == 1, user_list))

from collections import Counter
c = Counter()
c = Counter(user_list)

print("Метод 3 с условием - .get: ", 
      *filter(lambda x: c.get(x) == 1, c))

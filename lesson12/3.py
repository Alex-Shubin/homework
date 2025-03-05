"""

Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты(свойства):
    - value - текущее значение счетчика
    ...

Определить методы:
    - инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
    - increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
    - decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
    - reset, сбрасывает значение счетчика на стартовое    
    - метод __iter__
    - метод __next__
    
    * - stat, возвращает среднее количество изменений счетчика в секунду

"""
# ==========================================================
"""
1 вариант - с переменными:

self.start_time - старт
self.end_time - финиш - обновляется при каждом изменении счетчика
self.count_iter - счетчик изменений
"""
import random # если захочется рандомные числа
import time

class Counter:

    def __init__(self, start=0, end=3):
        self.value = start
        self.start_value = start
        self.end_value = end
        self.start_time = time.time() # переменная старта
        self.count_iter = 0

    def increase(self, num=1):
        self.value += num
        self.end_time = time.time() # записываем текущее время как конечное
        self.count_iter += 1
       

    def decrease(self, num=1):
        self.value -= num
        self.end_time = time.time() # записываем текущее время как конечное
        self.count_iter += 1

    def reset(self):
        self.value = self.start_value
        self.end_time = time.time() # записываем текущее время как конечное
        self.count_iter = 0

    def stat(self):

        result_time = self.end_time - self.start_time
        avg_changes_per_second = self.count_iter / result_time
        return avg_changes_per_second

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value < self.end_value:
            self.value += 1
            self.count_iter += 1
            self.end_time = time.time() # записываем текущее время как конечное
            return self.value 
        else:
            raise StopIteration
        
# a = Counter(random.randint(1, 10), random.randint(11, 20)*20)

a = Counter(10, 60)

a.increase(100) # счетчик +100

print(a.value)

a.decrease(60) # счетчик -60

print(a.value)

print("===========")

for i in a:

    print(i)

print(f"Среднее количество изменений в секунду: {a.stat():.4f}")
print(a.count_iter) # сколько всего было итераций


"""
2 - вариант - списком:

self.change_times - список, в который записывается каждое значение времени
метод record_change(self): - добавляет элемент в список
total_time - разница между последним и первым элементами списка
total_changes - количество элементов в списке

предполагаю, что при большом цикле список будет кушать много памяти.
но список позволяет сохранить значение в каждой итерации.

"""

# import random # если захочется рандомные числа
# import time

# class Counter:

#     def __init__(self, start=0, end=3):
#         self.value = start
#         self.start_value = start
#         self.end_value = end

#         self.change_times = [] # список времени изменений

#     def increase(self, num=1):
#         self.value += num
#         self.record_change() # записываем время в список

#     def decrease(self, num=1):
#         self.value -= num
#         self.record_change() # записываем время в список

#     def reset(self):
#         self.value = self.start_value
#         self.record_change() # записываем время в список

#     def record_change(self):
#         self.change_times.append(time.time()) # добавляем время в список

#     def stat(self):
#         if not self.change_times: # если список пуст - то 0
#             return 0
#         total_time = self.change_times[-1] - self.change_times[0] # список
#         total_changes = len(self.change_times) # список
#         avg_changes_per_second = total_changes / total_time # список
#         return avg_changes_per_second

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.value <self.end_value:
#             self.value += 1
#             self.record_change() # записываем время в список
#             return self.value
#         else:
#             raise StopIteration
        
# # a = Counter(random.randint(1, 10), random.randint(11, 20)*20)

# a = Counter(10, 55)

# a.increase(100) # счетчик +100

# print(a.value)

# a.decrease(60) # счетчик -60

# print(a.value)

# print("===========")

# for i in a:

#     print(i)

# print(f"Среднее количество изменений в секунду: {a.stat():.4f}")
# print(len(a.change_times)) # сколько всего было итераций
"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.
"""

user_mark = int(input("Введите оценку ученика: "))
mark_list = []

while user_mark != 0:
    mark_list.append(user_mark)
    user_mark = int(input("Введите следующую оценку: "))
    
print(f'Средний балл ученика {round(sum(mark_list) / len(mark_list), 1)}')

# 2 вариант

user_mark = 1
mark_list = []

while user_mark != 0:
    user_mark = int(input("Введите оценку ученика: "))
    mark_list.append(user_mark)
    
print(f'Средний балл ученика {round(sum(mark_list) / (len(mark_list) - 1), 1)}')
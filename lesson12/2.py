"""
Создать класс Student.


Определить атрибуты:
    - surname - фамилия
    - name - имя
    - group - номер группы
    - grads - список оценок

Определить методы:
    - инициализатор __init__
    - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
    студентов по среднему баллу
    - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
    - метод average_grade -считает и возвращает среднюю оценку ученика

Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 8
"""
from pprint import pprint

class Student:
    def __init__(self, surname:str, name:str, group:str|int, grads:list):
        self.surname = surname
        self.name = name
        self.group = group
        self.grads = grads

    def __eq__(self, other_student):
        return self.average_grade() == other_student.average_grade()
    
    def __ne__(self, other_student):
        return self.average_grade() != other_student.average_grade()
    
    def __lt__(self, other_student):
        return self.average_grade() < other_student.average_grade()
    
    def __gt__(self, other_student):
        return self.average_grade() > other_student.average_grade()
    
    def __le__(self, other_student):
        return self.average_grade() <= other_student.average_grade()
    
    def __ge__(self, other_student):
        return self.average_grade() >= other_student.average_grade()
    
    def add_grade(self, *grades):
        for grade in grades:
            if 1 <= grade <= 10:
                self.grads.append(grade)
            else:
                print(f"Оценка {grade} меньше 1 или больше 10")

    def average_grade(self):
        return sum(self.grads) / len(self.grads) if self.grads else 0
    
    def __str__(self):
        return f"{self.surname} {self.name}, группа {self.group}, средний балл: {self.average_grade():.2f}"
    
    def __repr__(self):
        return f"{self.surname} {self.name}, группа {self.group}, средний балл: {self.average_grade():.2f}"
    
def sort_students(students, reversed=False, best=None):
    """
    Сортирует список студентов по среднему баллу
    Args:
        students: список студентов для сортировки
        reversed: default=False, если True то в обратном порядке
        best: опционально, возвращает список студентов со средним баллом больше значения
    
    Returns:
        отсортированный список студентов
    """
    if best is not None:
        best_students = [student for student in students if student.average_grade() > best]
        if not best_students:
            return "нету таких"
        else:
            return best_students
    else:
        return sorted(students, reverse=reversed)
        
def print_students(students_list, message):
    """Печать списка студентов с сообщением как аргумент."""
    print(message)
    if isinstance(students_list, str): # если строка
        print(students_list)
    else:
        for student in students_list:
            print(student)
    
students = [
    Student("Кононов", "Сергей", "9a", [6, 6, 8, 9, 4, 9]),
    Student("Мефодий", "Суханов", "9b", [8, 3, 5, 8, 4, 8, 3, 3]),
    Student("Иванов", "Ратибор", "9a", [3, 8, 3, 10, 8, 10, 4, 7, 7, 6]),
    Student("Анастасия", "Селиверстова", "9b", [7, 9, 5, 4, 4, 7, 4, 6, 4, 4]),
    Student("Анжелика", "Быкова", "9a", [9, 6, 9, 10, 8, 8, 8, 9])
]

# создание отсортированного списка по возрастанию СБ и вывод
# students_sorted_asc = sort_students(students)
# print_students(students_sorted_asc, "Студенты, по возрастанию среднего балла:")

# создание отсортированного списка по убыванию СБ и вывод
# students_sorted_desc = sort_students(students, reversed=True)
# print_students(students_sorted_desc, "Студенты, по убыванию среднего балла:")

# создание отсортированного списка студентов со СБ выше 8
# best_students = sort_students(students, best=8)
# print_students(best_students, "Студенты со средним баллом больше 8:")


# добавил import pprint, def __repr__
# сортировка списка по возрастанию
pprint(sorted(students))
# сортировка списка по убыванию
pprint(sorted(students, reverse=True))
# студенты со средним баллом больше 8
print(*filter(lambda student: student.average_grade() > 8, students))
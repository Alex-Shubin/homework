'''
открыть и обработать файл students_grades.txt
собрать все данные в словарь ниже приведенного формата
записать в файл "excellent_students.txt" по 1 ученику из класса с наибольшим балом
{
    "9A":[
        {'fio':'fio', 
         'objects':{
            'mathematics':[4, 9, 7],
            'physics':[8, 9, 8, 6],
            ...:...
            }
        },
        ...        
    ],
    "9Б":[
        ...
    ]
}

'''
import re
from pprint import pprint

def split_with_quotes(line):
    parts = []
    current_part = ""
    quote_count = 0

    for char in line:
        if char == ",":
            if quote_count == 0:
                parts.append(current_part.strip())
                current_part = ""
            else:
                current_part += char
        elif char == "(":
            quote_count += 1
            current_part += char
        elif char == ")":
            quote_count -= 1
            current_part += char
        else:
            current_part += char

    parts.append(current_part.strip())
    return parts

def import_records(input_file):
    global students_data
    with open(input_file, "r", encoding="utf-8") as in_file:
        for line in in_file:
            line = line.strip()
            parts = split_with_quotes(line)
            fio = parts[0].strip()
            klass = parts[1].strip()
            grades = {}

            for i in range(2, len(parts)):
                subject_data = parts[i].strip()
                match = re.match(r"(.*)\s*(\(.*?\))", subject_data)
                subject = match.group(1).strip()
                grade_str = match.group(2).strip("()")
                grades[subject] = [int(g) for g in grade_str.split(',')]

            if klass not in students_data:
                students_data[klass] = []
            students_data[klass].append({
                "fio":fio,
                "subjects":grades
            })

def find_best_students(students_data):
    best_students = {}
    for klass, students in students_data.items():
        best_avg_grade = -1
        best_students_list = []

        for student in students:
            total_grades = 0
            total_subjects = 0
            for subject, grade_list in student['subjects'].items():
                total_grades += sum(grade_list)
                total_subjects += len(grade_list)

            if total_subjects > 0:
                avg_grade = total_grades / total_subjects
            else:
                avg_grade = 0

            if avg_grade > best_avg_grade:
                best_avg_grade = avg_grade
                best_students_list = [student['fio']]
            elif avg_grade == best_avg_grade:
                best_students_list.append(student['fio'])
        
        best_students[klass] = (best_students_list, best_avg_grade)
    return best_students

def write_best_students(best_students, output_file="lesson11\\excellent_students.txt"):
    with open(output_file, "w", encoding="utf-8") as out_file:
        for klass, (students, avg_grade) in best_students.items():
            out_file.write(f"Класс {klass}: ")
            if students:
                out_file.write(f"{", ".join(students)}, средний балл: {avg_grade:.2f}\n")
            else:
                out_file.write("нету таких\n")

students_data = {}
import_records("lesson11\\students_grades.txt")
best_students = find_best_students(students_data)
write_best_students(best_students)
pprint(best_students)
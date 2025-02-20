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

def process_records(input_file, output_file="lesson11\\excellent_students.txt"):
    global students_data
    with open(input_file, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            fio = parts[0].strip()
            klass = parts[1].strip()
            grades = {}

            for i in range(2, len(parts)):
                subject_data = parts[i].strip()
                match = re.match(r"(.*) \((.*)\)", subject_data)
                if match:
                    subject = match.group(1).strip()
                    grade_str = match.group(2)
                    grades[subject] = [int(g) for g in grade_str.split(",")]

            if klass not in students_data:
                students_data[klass] = []
            students_data[klass].append({
                "fio": fio,
                "objects": grades
            })

    excellent_students = {}
    for klass, students in students_data.items():
        best_student = None
        max_avg_grade = -1

        for student in students:
            total_grades = 0
            total_subjects = 0
            for subject, grade_list in student["objects"].items():
                total_grades = sum(grade_list)
                total_subjects = len(grade_list)

            if total_subjects > 0:
                avg_grade = total_grades / total_subjects
            else:
                avg_grade = 0

            if avg_grade > max_avg_grade:
                max_avg_grade = avg_grade
                best_student = student
        
        if best_student:
            excellent_students[klass] = best_student
    
    with open(output_file, "w", encoding="utf-8") as out_file:
        for klass, student in excellent_students.items():
            out_file.write(f"{klass}: {student["fio"]}\n")

students_data = {}
process_records("lesson11\\students_grades.txt")

print("Обработка завершена")

# pprint(students_data)
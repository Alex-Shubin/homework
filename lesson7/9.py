'''
*
В структуре данных из 5 урока задание №2 каждому сотруднику 
добавить к параметру "навык" параметр "мастерство" измеряемый от 0 до 100

Написать программу которая анализирует всю структуру данных и выводит сотрудников
с наибольшим параметром "мастерство" для каждого существующего навыка.
Пример вывода:
    1. Python - Иванов - 98
    2. JS - Петров  - 74     
    3. Базы данных - Николаев - 87     
    ...


** Пример вывода (перед выводам отсортировать по убыванию "мастерства"):
    
    --------------------------------------------------
    | № |   Навык     |       ФИО       | Мастерство |
    ==================================================
    | 1 | Python      | Иванов Н.С.     |     98     |
    | 2 | JS          | Петров В.В.     |     87     |
    | 3 | Базы данных | Николаев Е.Н.   |     74     |
    ...

 

'''

employees_list = [
    {"Name":"Сидоров В. М.",
    "Position":"директор",
    "Year of birth":"1973",
    "Skills":{
        "Python":"64",
        "Java":"75",
        "Org":"94"
        },   
    "Children":{
        "Child1":{
            "Name":"Петя",
            "Year of birth":"1994"
        },
        "Child2":{
            "Name":"Ира",
            "Year of birth":"1996"}
        }
    }, 
    {
    "Name":"Петров И. Ю.",
    "Position":"бухгалтер",
    "Year of birth":"1967",
    "Skills":{
        "SQL":"92",
        "1C":"97",
        "Python":"70"
        },
    "Children":{
        "Child1":{
            "Name":"Вася",
            "Year of birth":"1991"},
        "Child2":{
            "Name":"Коля",
            "Year of birth":"1998"}
        }
    }, 
    {
    "Name":"Иванова Ю. М.",
    "Position":"Front-End",
    "Year of birth":"1975",
    "Skills":{
        "JavaScript":"73",
        "HTML":"97",
        "PHP":"86"
        },
    "Children":{
        "Child1":{
            "Name":"Лера",
            "Year of birth": "1997"}
        }
    }
]

skills_list = list()

# 1 задание

for index, emp in enumerate(employees_list, 1):
    skills_list = list()
    for skill, val in emp["Skills"].items():
        skills_list.append((skill, emp["Name"], val))
        
    skills_list.sort(key=lambda x: x[2], reverse=True) # сорт скилл каждого юзера
    # вывод на печать 1 вариант
    print(f"{index}. {skills_list[0][0]} - {str(skills_list[0][1]).split()[0]} - {skills_list[0][2]}")
    

# 2 задание

for user in employees_list:
    for skill, val in user["Skills"].items():
        skills_list.append((skill, user["Name"], val))

# сортируем все навыки
skills_list.sort(key=lambda x: x[2], reverse=True)

# ширина 1 столбца
columns_len = []
columns_len.append(len(str(len(skills_list))))

# ширина 2, 3 и 4 столбца
skills = []
names = []
exps = []

for skill in skills_list:
    skills.append(len(skill[0]))
    names.append(len(skill[1]))
    exps.append(len(skill[2]))
columns_len.append(max(skills) if max(skills) >= len('Навык') else len('Навык'))
columns_len.append(max(names) if max(names) >= len('ФИО') else len('ФИО'))
columns_len.append(max(exps) if max(exps) >= len('Мастерство') else len('Мастерство'))

# печать шапки
print(f"{'-' * (sum(columns_len) + 13)}")
print(f"|{'№': ^{columns_len[0] + 2}}"
      f"|{'Навык': ^{columns_len[1] + 2}}"
      f"|{'ФИО': ^{columns_len[2] + 2}}"
      f"|{'Мастерство': ^{columns_len[3] + 2}}|"
      )
print(f"{'=' * (sum(columns_len) + 13)}")

# печать содержимого
for i, item in enumerate(skills_list):
    print(f"|{i+1: ^{columns_len[0] + 2}}"
          f"|{item[0]: ^{columns_len[1] + 2}}"
          f"|{item[1]: ^{columns_len[2] + 2}}"
          f"|{item[2]: ^{columns_len[3] + 2}}|"
          )
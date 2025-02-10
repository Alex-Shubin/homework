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
from pprint import pprint

employees_list = {
    1:{"Name":"Сидоров В. М.",
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
    2:{
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
    3:{
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
}

skills_list = list()

for user in employees_list:
    for skill, val in employees_list[user]["Skills"].items():
        skills_list.append((skill, employees_list[user]["Name"], val))

skills_list.sort(key=lambda x: x[2], reverse=True)

skills_dict = dict()

for index, item in enumerate(skills_list):
    new_item = [item[0], item[1].split()[0], item[2]]
    skills_dict.update({index:new_item})

for i in skills_dict:
    print(f"{i+1}. {' - '.join(skills_dict[i])}")

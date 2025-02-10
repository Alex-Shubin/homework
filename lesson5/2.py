"""
2. Создать структуру данных сотрудников фирмы с 
    тремя сотрудниками. каждый сотрудник должен иметь:
        ФИО, 
        должность, 
        год рождения, 
        список навыков, 
        список детей с их именем и годом рождения. 
    
    Запросить ФИО сотрудника и вывести по нему информацию.
"""
employees_list = {
    1:{"Name":"Сидоров В. М.",
    "Function":"директор",
    "Year of birth":"1973",
    "Skills":"руками водит",
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
    "Function":"бухгалтер",
    "Year of birth":"1967",
    "Skills":"хорошо считает",
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
    "Function":"уборщица",
    "Year of birth":"1975",
    "Skills":"хорошо убирает",
    "Children":{
        "Child1":{
            "Name":"Лера",
            "Year of birth": "1997"}
        }
    }
}

employee_request = input("Введите ФИО сотрудника: ")

# employee_request = "Иванова Ю. М."

selected_employee = list(filter(lambda x: employee_request in employees_list[x]["Name"], employees_list))[0]

from pprint import pprint

pprint(employees_list[selected_employee])

# pprint(employees_list[list(filter(lambda x: employee_request in employees_list[x]["ФИО"], employees_list))[0]])
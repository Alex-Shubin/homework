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

employee1 = {
    "ФИО":"Сидоров В. М.",
    "должность":"директор",
    "год рождения":"1973",
    "список навыков":"руками водит",
    "дети":{
        "ребенок1":{
            "имя":"Петя",
            "год рождения":"1994"
        },
        "ребенок2":{
            "имя":"Ира",
            "год рождения":"1996"
        }
    }
}
employee2 = {
    "ФИО":"Петров И. Ю.",
    "должность":"бухгалтер",
    "год рождения":"1967",
    "список навыков":"хорошо считает",
    "дети":{
        "ребенок1":{
            "имя":"Вася",
            "год рождения":"1991"
        },
        "ребенок2":{
            "имя":"Коля",
            "год рождения":"1998"
        }
    }
}
employee3 = {
    "ФИО":"Иванова Ю. М.",
    "должность":"уборщица",
    "год рождения":"1975",
    "список навыков":"хорошо убирает",
    "дети":{
        "ребенок1":{
            "имя":"Лера",
            "год рождения": "1997"
        }
    }
}

employees_list = {1:employee1, 2:employee2, 3:employee3}

employee_request = input("Введите ФИО сотрудника: ")

selected_employee = list(filter(lambda x: employee_request in employees_list[x]["ФИО"], employees_list))

print(selected_employee)
print(employees_list[selected_employee[0]])

# не понимаю как сделать без filter, который возвращает только list
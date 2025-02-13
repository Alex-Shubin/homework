"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""
users_list = [
    {"name":"Vasya",
     "login":"vas",
     "password":"123456"
     },
     {"name":"Denis",
      "login":"Denis123",
      "password":"qwer"
     },
     {"name":"Petya",
      "login":"Petr.1",
      "password":"password"
     }
]

wrong_pass = list(filter(lambda user: len(user["password"]) < 5, users_list))
print(wrong_pass)
# [{'name': 'Denis', 'login': 'Denis123', 'password': 'qwer'}]
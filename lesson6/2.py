'''
запросить у пользователя логин пароль и возраст
вывести доступ разрешен:
    логин:admin   пароль:123456    возраст: любой    
    логин:vasya   пароль: vas123   возраст: менее 60
    логин:guest   пароль: любой    возраст:более 18
    
в остальных случаях - "доступ запрещен".

'''
user_login = input("Введите логин: ")
user_pass = input("Введите пароль: ")
user_age = int(input("Сколько вам лет? "))

if (user_login == "admin" and user_pass == "123456"):
    print("доступ разрешен")
elif (user_login == "vasya" and user_pass == "vas123" and user_age < 60):
        print("доступ разрешен")
elif (user_login == "guest" and user_age > 18):
        print("доступ разрешен")
else: 
    print("доступ запрещен")
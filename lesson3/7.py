user_login = input("Введите ваш логин: ")
user_password = input("Введите ваш пароль: ")

correct_user_login = user_login == "admin"
correct_user_password = user_password == "12345"

print(f"Логин:{correct_user_login} / Пароль:{correct_user_password}")
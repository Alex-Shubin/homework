'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''
# user_num1 = int(input("Введите первое число: "))
# user_num2 = int(input("Введите второе число: "))
# user_num3 = int(input("Введите третье число: "))

user_num1 = 4
user_num2 = 3
user_num3 = 4

if user_num1 == user_num2 == user_num3:
    print("нет наибольшего числа")
elif user_num1 >= user_num2 and user_num3:
    print(user_num1)
elif user_num2 >= user_num1 and user_num3:
    print(user_num2)
elif user_num3 >= user_num1 and user_num2:
        print(user_num3)
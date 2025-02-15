'''
Запросить у пользователя число
    - если число менее 20 -  вывести на экран сколько чисел 
        в диапазоне от 0 до этого числа делится без остатка на 7. 
    - если более 20 - вывести на экран сколько чисел 
        в диапазоне от 0 до этого числа делится без остатка на 11.
'''
user_number = abs(int(round(float((input("Введите любое число: "))))))

print(user_number // 7 if user_number < 20 else 11)

if user_number == 20:
    print(f"для числа {user_number} нет правила")
else:
    print(f"Вы ввели {user_number}")

# старый вариант

# if user_number < 20:
#     print(f"{user_number // 7} чисел в диапазоне от 0 до {user_number} делится на 7")
# elif user_number > 20:
#     print(f"{user_number // 11} чисел в диапазоне от 0 до {user_number} делится на 11")
# elif user_number == 20:
#     print(f"для числа {user_number} нет правила")
# else:
#     print(f"Вы ввели {user_number}")
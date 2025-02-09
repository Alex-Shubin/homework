"""
*
Написать программу калькулятор которая предлагает 
ввести пример для решения пока пользователь не введет команду "стоп"
Программа должна решить пример и запросить следующий.
При вводе команды "стоп" программа завершается.
Поддерживаемые операции: + - * ** /
Пример:
    Введите пример или 'стоп' для завершения: 2 + 2
    Ответ: 4
    Введите пример или 'стоп' для завершения: 16 / 8
    Ответ: 2
    Введите пример или 'стоп' для завершения: 1651+
    Неправильный формат. Пример: '2 + 4'

"""
while True:
    user_example = input("Введите пример вида '2 + 2' или 'стоп' для выхода: ")
    # проверка на "стоп"
    if user_example.lower() == "стоп":
        break
    # прверка на правильность ввода
    if len(user_example.split()) < 3:
        print("Неправильный формат. Пример: '2 + 4'") 
        continue
    else:
        calc_list = user_example.split()
        for i in calc_list:
            if i in ("+", "-", "*", "/", "**"):
                if i == "+":
                    result = int(calc_list[0]) + int(calc_list[2])
                    break
                elif i == "-":
                    result = int(calc_list[0]) - int(calc_list[2])
                    break
                elif i == "*":
                    result = int(calc_list[0]) * int(calc_list[2])
                    break
                elif i == "/":
                    # проверка деления на 0
                    if int(calc_list[2]) == 0:
                        print("Деление на 0! Попробуйте еще раз")
                        result = ""
                        break
                    # убираем .0 если поделилось без остатка
                    if int(calc_list[0]) % int(calc_list[2]) == 0:
                        result = int(int(calc_list[0]) / int(calc_list[2]))
                        break
                    result = int(calc_list[0]) / int(calc_list[2])
                    break
                elif i == "**":
                    result = int(calc_list[0]) ** int(calc_list[2])
                    break
    
    if result:
        print(f"Ответ: {result}" )

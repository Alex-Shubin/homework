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
operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "**": lambda a, b: a ** b
}

while True:
    res = 0
    user_example = input("Введите пример вида '2 + 2' или 'стоп' для выхода: ")
    # проверка на "стоп"
    if user_example.lower() == "стоп":
        break
    # проверка на правильность ввода
    if len(user_example.split()) < 3:
        print("Неправильный формат. Пример: '2 + 4'") 
        continue
    # вычисления
    else:
        text_plus = "+"
        calc_list = user_example.split()
        for i in calc_list:
            if i in ["+", "-", "*", "/", "**"]:
                # проверка деления на 0
                if i == "/" and calc_list[2] == "0":
                    print("Деление на 0! Попробуйте еще раз")
                    res = 0
                    break
                else:
                    text_plus = i
            else:
                res = operators[text_plus](res, float(i))
    
    if res:
        print(f"Ответ: {int(res) if res - int(res) == 0 else res}" )
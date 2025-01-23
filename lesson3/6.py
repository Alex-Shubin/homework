user_value1 = int(input("Введите первое число: "))
user_value2 = int(input("Введите второе число: "))
user_value3 = int(input("Введите третье число: "))

result = round(((user_value1 + user_value2 + user_value3) / 3), 3)

print("Среднее арифметическое 3 чисел = " + str(result))
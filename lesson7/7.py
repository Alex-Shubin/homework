"""
Запросить любое число не менее 10. 
Вывести на экран сумму квадратов каждой цифры составляющей это число. 
Например: дано 236 => 2*2 + 3*3 + 6*6 = 49 

"""
user_number = 1

while user_number < 10:
    user_number = int(input("Введите число больше 10: "))

result = 0
numbers_list = list()
calculation = list()

for n in str(user_number):
    result += int(n) * int(n)
    numbers_list.append(int(n))
    calculation.append(f"{n}*{n}")

print(f"дано {user_number} => {' + '.join(calculation)} = {result}")
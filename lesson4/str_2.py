'''
Программа должна запросить несколько цифр через пробел 
    - выдать их общую сумму
    - выдать максимальную цифру
    - выдать среднее арифметическое

'''
user_numbers_input = input("Введите несколько цифр через пробел: ")

user_numbers_list = list(map(int, user_numbers_input.split()))

print(f"Общая сумма = {sum(user_numbers_list)}")
print(f"Максимальная цифра = {max(user_numbers_list)}")
print(f"Арифметическое среднее = {sum(user_numbers_list)/len(user_numbers_list)}")

'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Например: 1352=aceb.
'''
abcd = {
    1:'a',
    2:'b',
    3:'c',
    4:'d',
    5:'e',
    6:'f',
    7:'g',
    8:'h',
    9:'i',
    0:'j'
}

user_number = input("Введите любое число: ")
result_word = ""

for number in user_number:
    result_word += abcd.get(int(number))

print(f"{user_number}={result_word}")
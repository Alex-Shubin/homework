'''

Дан списк:
['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
Для каждого элемента в списке 
    - вывести на экран сначала номер элемента 
    - сам элемент 
    - символ данного элемента, соответствующий номеру его позиции в списке. 
Образец:
1 - qwertyu - q
2 - asdfggh - s
3 - zxcvbnm - c
и так далее...


'''
user_list = ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']

for i, word in enumerate(user_list):
    print(f"{i + 1} - {user_list[i]} - {user_list[i][i]}")
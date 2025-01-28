'''
Дан произвольный список. Вывести на экран в обратном порядке. 
Задачу решить 2мя способами. 
'''
user_list = list(input("Введите несколько значений: "))

# 1
user_list_1 = user_list[::-1]
print(user_list_1)

# 2
import copy
# print(user_list) # проверка начального списка
user_list_2 = copy.deepcopy(user_list)
user_list_2.reverse()
print(user_list_2)

# 3
# print(user_list) # проверка начального списка
user_list_3 = copy.deepcopy(user_list)
user_list_3 = reversed(user_list_3)
print(list(user_list_3))
# print(user_list) # проверка начального списка

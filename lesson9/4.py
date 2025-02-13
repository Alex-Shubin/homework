'''
Дан список [1,2,3,4,5,6,7,8,9]. Создать 3 копии этого списка 
и с каждой выполнить след действия:
    - возвести каждый элемент во 2ю степень
    - прибавить 3 к каждому элементу значение которого является четным 
    - элементы значения которого является 
            четными - умножить на 2 
            нечетным - умножить на 3

Использовать map и lambda.
'''
init_list = [1,2,3,4,5,6,7,8,9]

exp_list = list(map(lambda i: i ** 2, init_list.copy()))
# print(exp_list) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

sum_list = list(map(lambda i: i + 3 if i % 2 == 0 else i, init_list.copy()))
# print(sum_list) # [1, 5, 3, 7, 5, 9, 7, 11, 9]

# sum_list = list(map(lambda i: i + 3, filter(lambda x: x % 2 == 0, init_list.copy())))
# print(sum_list) # [5, 7, 9, 11]

even_odd_list = (list(map(lambda i: i * 2 if i % 2 == 0 
                          else i * 3, init_list.copy())))
# print(even_odd_list) # [3, 4, 9, 8, 15, 12, 21, 16, 27]
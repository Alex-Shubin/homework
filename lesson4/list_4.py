'''
Дан список:
['hello', 'python', 'интерпретатор', 'pep8', "123"]
Вернуть список где вместо элементов данного списка прописаны количество символов каждого элемента.

'''
some_list = ['hello', 'python', 'интерпретатор', 'pep8', "123"]

# тренировался
# edited_list = []
# for i in some_list:
#     edited_list.append(len(i))
# print(edited_list)

print(list(map(lambda x: len(x), some_list)))


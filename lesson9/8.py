'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''
some_list = [1, 2, 3, 4, "qwe", "rty", False, 3.21, True]

str_list = list(filter(lambda x: isinstance(x, str), some_list))
print(str_list) # ['qwe', 'rty']

bool_list = list(filter(lambda x: isinstance(x, bool), some_list))
print(bool_list) # [False, True]
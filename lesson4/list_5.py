'''
Дан список
['samsung', 'lg', 'xerox', 'bosch']
Удалить элемент с именем 'xerox'
Добавить элемент на 2 место 'indesit'

'''
some_list = ['samsung', 'lg', 'xerox', 'bosch']
some_list.remove('xerox')
some_list.insert(1, 'indesit')
print(some_list)
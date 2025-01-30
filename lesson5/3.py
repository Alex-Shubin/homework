"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.

"""
d = {'one':11, 'two':22, 'hello':'python', True:False}

del_request = int(input("Введите номер для удаления: "))

del d[list(d.keys())[del_request]]

print(d)
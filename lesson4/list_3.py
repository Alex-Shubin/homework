'''
Дан произвольный список из 5 элементов. 
     - Поменять местами 1ый и последний элемент
     - удалить и вывести на печать третий элемент
'''
list_items = [1, 3, 5, 7, 9]
list_items[0], list_items[-1] = list_items[-1], list_items[0]
print(list_items.pop(2))
print(list_items)
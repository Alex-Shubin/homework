'''
Запросить по очереди у пользователя 5 имен. Добавить все в список. 
Отсортировать. 
Вывести на экран.
Вывести True при наличии в списке имени 'Вася'
'''
username_list = list() 
username_list.append(input("Введите первое имя: "))
username_list.append(input("Введите второе имя: "))
username_list.append(input("Введите третье имя: "))
username_list.append(input("Введите четвертое имя: "))
username_list.append(input("Введите пятое имя: "))

username_list.sort()
print(username_list)
correct_username = "Вася" in username_list
if correct_username == True: print("True")

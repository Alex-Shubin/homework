"""
Запросить трижды ввод наименования товаров и их цену через пробел. 
"пример: 
>>>яблоко 10"
>>>груша 15
>>>малина 20
    
    - создать из введенных данных словарь где ключ это наименование, а цена значение
    - запросить имя товара, найти его в словаре, и вывести его цену, увеличенную на 15%. 
    - вывести сумму всех товаров

"""
item_list1 = input("Введите название товара и цену через пробел: ").split()
item_list2 = input("Введите название товара и цену через пробел: ").split()
item_list3 = input("Введите название товара и цену через пробел: ").split()

dict_item_price = (dict([item_list1, item_list2, item_list3]))

item_name = input("Введите название товара: ")

print(f"Цена {item_name} = {float(dict_item_price[item_name])*1.15}")
print(f"Сумма всех товаров = {sum(map(float, dict_item_price.values()))}")




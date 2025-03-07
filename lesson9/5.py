'''
*
Написать рекурсивную функцию, которая принимает список 
и печатает каждых элемент на новой строке. 
Если элемент списка - список, то его элементы должны выводиться 
с отступом относительно родительского на 2 символа. 
Символ для отступа передать дополнительными необязательным параметром.

** написать такую же функцию но без рекурсии

Пример1: some_list = [1, 2, 3, [4, [5, 6], 7], 8, 9]
1
2
3
--4
----5
----6
--7
8
9

Пример2: some_list=[1,[2,[[3],4]],5,[[[6,7]]],8,[[[[9,10]],11]],12]
1
--2
------3
----4
5
------6
------7
8
--------9
--------10
----11
12

'''
import inspect

def sort_list_rek(some_list=list, sym="-"):
    for num in some_list:
        if isinstance(num, list):
            sort_list_rek(num)
        else:
            print(sym * (len(inspect.getouterframes(inspect.currentframe()))-2) * 2 + str(num))
    return

def sort_list(some_list=list, sym="-"):
    str_list = str(some_list)
    indent = 0
    result = ""
    for item in str_list:
        if item.isdigit():
            result = result + item
        else:
            if result:
                print(f"{sym * (indent - 1) * 2}{result}")
                result = ""
            if item == "[":
                indent += 1
            elif item == "]":
                indent -= 1
            elif item == "," or " ":
                pass
                

# some_list = [1, 2, 3, [4, [5, 6], 7], 8, 9]
some_list=[1,[2,[[3],4]],5,[[[6,7]]],8,[[[[9,10]],11]],12]

# sort_list_rek(some_list)
sort_list(some_list)


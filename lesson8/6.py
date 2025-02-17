"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""
def yes_or_no(num_list:list):
    if all(isinstance(num, int) for num in num_list):
        num_set = set()
        yes_list = list()
        for i in num_list:
            yes_list.append("yes" if i in num_set else "no")
            num_set.add(i)
        return yes_list
    else:
        return False
        
ex_list = [1, 2, 3, 4, 2, 3]

print(yes_or_no(ex_list))


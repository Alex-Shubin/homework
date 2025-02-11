"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев


"""
def change_name(user_name:str, is_reversed=False):
    name_list = user_name.split()
    name_list[1] = name_list[1][0] + "."
    name_list[2] = name_list[2][0] + "."
    if is_reversed:
        name_list[0], name_list[1], name_list[2] = name_list[1], name_list[2], name_list[0]
        return ' '.join(name_list)
    else:
        return ' '.join(name_list)

# user_string = "Васечкин Петр Николаевич"

# result_name = change_name(user_string, False)

# print(f"-  {result_name}")

























# ------------in work-------------

# def change_name(user_name:str, is_reversed:bool):
#     name_dict = {
#         "LastName":user_name.split()[0],
#         "FirstName":user_name.split()[1],
#         "SecondName":user_name.split()[2]
#     }
#     return 
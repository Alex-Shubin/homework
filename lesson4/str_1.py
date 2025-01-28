'''
Программа должна запросить любую фразу и вывести на экран :
     - количество символов в данной фразе.
     - количество слов  в данной фразе. 
            Словом может считаться любой набор символов разделенный от 
            других пробелом и количеством символов больше или равных 1.
     -* количество гласных в данной фразе. Нельзя использовать if и for.

'''

user_string = input("Напишите любую фразу из нескольких слов: \n")
print(f"В этой фразе {len(user_string)} символов")
print(f"В этой фразе {len(user_string.split(" "))} слов/слова")

user_string = user_string.lower()

print(f"В этой фразе {
    len(list(filter(lambda x: x in "ауоиэыяюеёaeiouy", user_string)))
    } гласных букв")

# разбираюсь с lambda
# test_list = list(filter(lambda x: x in "ауоиэыяюеёaeiouy", user_string))
# print(test_list)

print(f"В этой фразе {sum(map(user_string.count, "ауоиэыяюеёaeiouy"))} гласных")

# разбираюсь с map
# test_list = list(map(user_string.count, "ауоиэыяюеёaeiouy"))
# print(test_list)
'''
Буква "a" стоит 10 очков, "b" - 20, "c" - 30, "d" - 40
Запросить кодовою фразу из пяти символов используя только a, b, c, d.
Вывести на экран общее количество очков введенной фразы.

'''
abcd = {"a":10,
        "b":20,
        "c":30,
        "d":40
        }

sum_request = input("Введите фразу из 5 букв, используя символы a b c d: ")

# sum_request = "ddddd"

print(sum(list(map(lambda x: abcd.get(x), sum_request))))

print(sum(list(map(abcd.get, sum_request)))) # без лямбды - подкидывает каждый элемент из итерации как аргумент функции

print(sum(list((abcd[x] for x in sum_request)))) # то же самое


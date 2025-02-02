"""
Запросить фразу 
    - вывести на экран количество уникальных символов
    - вывести на экран количество уникальных слов
    -* вывести символ который встречался чаще всего

"""
user_input = input("Введите фразу из нескольких слов: ")
# user_input = "Некоторая фраза фраза"

print(f"В этой фразе {len(set(user_input))} уникальных символов")
print(f"В этой фразе {len(set(list(user_input.split())))} уникальных слов(-а)")

user_dict = {x: user_input.count(x) for x in user_input}

max = max(list(user_dict.values()))
max_key = list(filter(lambda key: user_dict[key] == max, user_dict))

# этот метод сработает, если наиболее используемых символов несколько
print(f"Символ {max_key} встречался чаще всего ({max} раз)")

# а тут через Counter - покажет только 1 символ

from collections import Counter
c = Counter()
c = Counter(user_input)

# sorted(c.elements()) # не нужно

print(f"Чаще всего встречался символ {c.most_common(1)}")
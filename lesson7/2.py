'''
Запросить фразу состоящую минимум из трех слов. 
Сформировать фразу из этих слов в которой каждая буква слова, 
продублирована то количество раз, которое соответствует номеру позиции 
данной буквы в слове этой буквы. 
Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа

'''

user_string = input("Введите фразу из 3 слов: ").split()
# user_string = ['qwe', 'asd', 'zxc']

words_list = []

for word in user_string:
    letters = ""
    for index, letter in enumerate(word, 1):
        letters += letter * index
    words_list.append(letters)

print(*words_list)
print(f"{" ".join(words_list)}")
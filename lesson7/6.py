"""
1. Запросить у пользователей имя и отзыв о магазине. 
Программа должна запрашивать данные пока не введено слово "stop". 
Все данные сложить в словарь.
    -распечатать количество отзывов
    -распечатать отдельно имена пользователей
    -распечатать отдельно отзывы

"""
user_reviews = {}

while True:
    user_name = input("Введите ваше имя: ")
    if user_name == "stop":
        break
    user_review = input("Ваш отзыв: ")
    if user_review == "stop":
        break
    this_review = {user_name: user_review}
    user_reviews.update(this_review)

print(f"Всего отзывов: {len(user_reviews)}")

print("Имена пользователей:")
for key in user_reviews.keys():
    print(key)

print("Отзывы:")
for val in user_reviews.values():
    print(val, "\n")
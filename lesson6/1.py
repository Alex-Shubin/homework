"""
Запросить у пользователя год рождения и в соответствии с его возрастом 
охарактеризовать пользователя - 
ребенок, подросток, юноша, в расцвете сил, пожилой, старик.
"""
from datetime import datetime

year_of_birth = int(input("Ваш год рождения? "))
user_age = datetime.now().year - year_of_birth

if user_age >= 0:
    if 0 <= user_age <= 10: 
        print("Вы ребенок")
    elif user_age <= 18: 
        print("Вы подросток")
    elif user_age <= 21:
        print("Вы юноша/девушка")
    elif user_age <= 55:
        print("Вы в расцвете сил")
    elif user_age <= 75:
        print("Вы пожилой человек")
    elif user_age <= 90:
        print("Вы старик")
    elif 90 < user_age:
        print("Вы долгожитель!")
else:
    print("Вы еще не родились?")

"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""
days_dict = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}

# в порядке возрастания
sorted_days_dict = dict(sorted(list(days_dict.items()), key=lambda d: d[1]))
print(sorted_days_dict)

# и обратно
sorted_r_days_dict = (dict(sorted(list(days_dict.items()), 
                                  key=lambda d: d[1], reverse=True)))
print(sorted_r_days_dict)

"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""
a1 = 1
a2 = 2.2
a3 = 3
a4 = 4.1

print("All Float:", all(map(lambda x: isinstance(x, float), [a1, a2, a3, a4])))

if all(isinstance(a, float) for a in (a1, a2, a3, a4)):
    print("True Float")

print("Some String:", any(map(lambda x: isinstance(x, str), [a1, a2, a3, a4])))

if any(isinstance(a, str) for a in (a1, a2, a3, a4)):
    print("True String")

pairs = [(a1, a3), (a2, a4), (a3, a4)]
print("Int Pairs:", any(map(lambda x: isinstance(x[0], int) and isinstance(x[1], int), pairs)))

if any(isinstance(a[0], int) and isinstance(a[1], int) for a in pairs):
    print("True Int")


# if (isinstance(a1, float) 
#     and isinstance(a2, float) 
#     and isinstance(a3, float) 
#     and isinstance(a4, float)):
#     print("True Float")
# elif (isinstance(a1, str) 
#       or isinstance(a2, str) 
#       or isinstance(a3, str) 
#       or isinstance(a4, str)):
#     print("True Str")
# elif ((isinstance(a1, int) and isinstance(a3, int)) 
#       or (isinstance(a2, int) and isinstance(a4, int)) 
#       or (isinstance(a3, int) and isinstance(a4, int))):
#     print("True Int pairs")

# с type(x) не работает - почему??

# if type(a1) and type(a2) and type(a3) and type(a4) == float:
#     print("True Float")
# el if type(a1) or type(a2) or type(a3) or type(a4) == str:
#     print("True Str")
# if (type(a1) and type(a3)) or (type(a2) and type(a4)) or (type(a3) and type(a4)) == int:
#     print("True Int pairs")

# ниже дежурные записи, чтобы потом подглядывать

# a_float = True if isinstance(a1, float) and isinstance(a2, float) and isinstance(a3, float) and isinstance(a4, float) else False
# a_str = True if isinstance(a1, str) or isinstance(a2, str) or isinstance(a3, str) or isinstance(a4, str) else False
# a_int = True if (isinstance(a1, int) and isinstance(a3, int)) or (isinstance(a2, int) and isinstance(a4, int)) or (isinstance(a3, int) and isinstance(a4, int)) else False

# print(f"Float - {a_float},\nString - {a_str},\nInteger pairs - {a_int}")
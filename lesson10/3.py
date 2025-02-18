"""
Написать функцию которая принимает строку в которой есть 
круглые скобки и возвращает True или False анализируя все ли скобки 
являются закрытыми и расставлены в правильном порядке.
Примеры:
    (()()) -> True
    (()()() -> False
    (hello(2)ver()(33)python) -> True
    (hello(2()ver(33)python)) -> True
    (hello(2()ver(33)python) -> False

"""
def check_brackets(some_str):
    good = 0

    for sym in some_str:
        if sym == "(":
            good += 1
        elif sym == ")":
            good -= 1
        
    return True if good == 0 else False

print(check_brackets("(()())"))
print(check_brackets("(()()()"))
print(check_brackets("(hello(2)ver()(33)python)"))
print(check_brackets("(hello(2()ver(33)python))"))
print(check_brackets("(hello(2()ver(33)python)"))
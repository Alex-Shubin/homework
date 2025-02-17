"""
Написать функцию (без регулярных выражений), которая принимает текстовую строку 
и возвращает словарь, который содержит информацию о количестве 
символов, слов, строк и предложений в тексте. 
Затем создайте вторую функцию, которая принимает этот словарь, 
и выводит его содержимое в удобном и красивом формате. 

"""
def to_dict(string:str):
    str_dict = {
        "Symbols":len(string),
        "Words":len(string.split()),
        "Lines":len(string.split("\n")),
        "Sentences":len(string.split("."))
    }
    return str_dict

def to_print(str_dict:dict):
    keys_w = max(list(len(key) for key in str_dict.keys()))
    values_w = max(list(len(str(value)) for value in str_dict.values()))
    print(f"{'-' * (keys_w + values_w + 7)}")
    for key, value in str_dict.items():
        print(f"| {key: <{keys_w}} | {value: >{values_w}} |")


to_print(to_dict("""where nnnn is the code point in decimal form, 
                 and hhhh is the code point in hexadecimal form. 
                 The x must be lowercase in XML documents. 
                 The nnnn or hhhh may be any number of digits 
                 and may include leading zeros. The hhhh may mix uppercase and lowercase, 
                 though uppercase is the usual style.
                 In contrast, a character entity reference refers to a character 
                 by the name of an entity which has the desired character 
                 as its replacement text. The entity must either be predefined 
                 (built into the markup language) or explicitly declared in a 
                 Document Type Definition (DTD). The format is the same as for 
                 any entity reference:
                 &name;
                 where name is the case-sensitive name of the entity. The semicolon is required."""))
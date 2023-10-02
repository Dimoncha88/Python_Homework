# Напишите функцию принимающую на вход только ключевые параметры и 
# возвращающую словарь, где ключ — значение переданного аргумента, 
# а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def new_dict(**kwargs):

    my_dict = {}

    for key, val in kwargs.items():
        if not isinstance(val, (int, float,str, tuple, frozenset)):
            val = str(val)
        my_dict[val] = key
    return my_dict

print(new_dict(a=1, b='Hi', c=[1, 2, 3]))
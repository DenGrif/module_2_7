def print_params(a=1, b='строка', c=True):
    print(f'a = {a}, b = {b}, c = {c}')

# 1. Функции с разным количеством аргументов
print_params()
print_params(10)
print_params(10, 'Строка 2')
print_params(10, 'Строка 2', False)
print_params(b=25)
print_params(c=[1, 2, 3])

# 2. Распаковка параметров
values_list = [42, 'example', False]
values_dict = {'a': 100, 'b': 'example_dict', 'c': [10, 20, 30]}

print_params(*values_list)
print_params(**values_dict)

# 3. Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)

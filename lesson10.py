# Задача 1
# Дано список словорей
# [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
# создать список кортежей
# [('red', 'high'), ('yellow', 'low')]
colors = [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
new_list1 = [tuple(dict_.values()) for dict_ in colors]
print(new_list1)

# Задача 2
# Дано словарь
# a_dictionary = {"a": 1, "b": 2, "c": 3}
# преобразовать его в список кортежей
# [('a', 1), ('b', 2), ('c', 3)]
a_dictionary = {"a": 1, "b": 2, "c": 3}
my_list_of_tuples = [value for value in a_dictionary.items()]
print(my_list_of_tuples)


# Задача 3
# Дано два списка
# list_a = [1, 2, 3, 4]
# list_b = [5, 6, 7, 8]
# Создать из них список кортежей
# list_c = [(1,5), (2,6), (3,7), (4,8)]
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
list_c = list(zip(list_a, list_b))
print(list_c)

# Задача 4
# Дано словарь
# {1:'entry 1', 2:'entry 2', 3:'entry 3', 4:'entry 4'}
# Создать кортеж занчений для первих трьох єлементов словоря
user_entry = {1: 'entry 1', 2: 'entry 2', 3: 'entry 3', 4: 'entry 4'}
my_tuple = tuple(list(user_entry.values())[0:3])
print(my_tuple)

# Задача 5
# Дано список
# ["bar", "baz", "qux", "etc"]
# Создать кортеж
# ("foo", "bar", "baz", "qux", "etc")
given_list = ["bar", "baz", "qux", "etc"]
answer = ('foo',) + tuple(elem for elem in given_list)
print(answer)

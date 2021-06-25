from random import randint

# Создайте словарь с количеством элементов не менее 5-ти.
# Поменяйте местами первый и последний элемент объекта.
# Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
# Выведите на печать итоговый
# словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
my_dict = {'element1': '1', 'element2': '2', 'element3': '3', 'element4': '4', 'element5': '5'}
print(id(my_dict))
first = list(my_dict.items())[0]
last = list(my_dict.items())[-1]
second = list(my_dict.items())[1]
print(second)
my_dict[first[0]] = last[1]
my_dict[last[0]] = first[1]
my_dict.pop(second[0])
my_dict['new_key'] = 'new_value'
print(my_dict)
print(id(my_dict))


# Как получить значение по ключу 'marks' словаря student = {'name': 'Emma', 'class': 9, 'marks': 75}
student = {'name': 'Emma', 'class': 9, 'marks': 75}
marks = student['marks']
print(marks)

# Что выведет этот код? p = {'name': 'Mike', 'salary': 8000} print(p.get('age')).
p = {'name': 'Mike', 'salary': 8000}
# этот код выведет None
print(p.get('age'))

# Как получить 'd':sample = {'1':['a','b'], '2':['c','d']}.
sample = {'1': ['a', 'b'], 
          '2': ['c', 'd']}
result = sample['2'][1]
print(result)

# Дан список стран и городов каждой страны. Затем дан cсмписок названия городов. Для каждого города укажите,
# в какой стране он находится. list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио",
# "Германия-Мюнхен"], list_2 = ["Киев", "Токио", "Минск"] Получить dict_ = ["Украина": "Киев", "Япония": "Токио",
# "Беларусь": "Минск"]
list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"]
list_2 = ["Киев", "Токио", "Минск"]
my_dict = {}
dict_ = {}

for country_city in list_1:
    separator = country_city.split('-')
    my_dict[separator[1]] = separator[0]

for city in list_2:
    if city in my_dict.keys():
        country = my_dict[city]
        dict_[my_dict[city]] = city

print(dict_)

# Для английского алфовита сгенерировать словарь-шифратор, то есть словарь, где ключ буква алфавита, а значение
# являются случайное значение. Используя словарь, зашифровать/расшифровать введенное сообщение.
sypher = {}
list_ = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(',')
list_4 = [' ']
message = 'My name is Dmitriy'
encoded_result = []
decoded_list = []

for i in list_:
    list_4.append(i)
    list_4.append(i.lower())

for i in list_4:
    sypher[i] = randint(1, 9999)

for letter in message:
    for key in sypher:
        if key == letter:
            encoded_result.append(sypher[key])

for encoded_letter in encoded_result:
    for key, value in sypher.items():
        if encoded_letter == value:
            decoded_list.append(key)

joining = ''.join(decoded_list)
print(encoded_result)
print(joining)

# Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
number = range(1, 11)
cubic_nums = {n: n**3 for n in number}
print(cubic_nums)

# Создайте словарь из строки следующим образом: в качестве ключей возьмите буквы строки, а значениями пусть будут
# числа, соответствующие количеству вхождений данной буквы в строку.
my_string = "Шла Саша по шоссе и сосала сушку"
keys = set(my_string.lower().replace(' ', ''))
symbol_count = {}
for symbol in keys:
    symbol_count[symbol] = my_string.lower().count(symbol)
print(symbol_count)

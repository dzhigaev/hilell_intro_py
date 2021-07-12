# Задан некоторый список A содержащий целые числа.
# Pазработать программу, которая вычисляет сумму элементов списка.
A = [1, 3, 4, 10, 9000, 100]
result = 0
for element in A:
    result = element + result
print(result)

# Задан список строк. В каждой строке подсчитать количество вхождений заданного символа
list_of_strings = ['asdfg', '12345', 'Hello', 'world', 'random string']
given_symbol = 'r'
for element1 in list_of_strings:
    result1 = element1.count(given_symbol)
    print(f'in \'{element1}\': giver string was found {result1} times')
# Пользователь вводит число. Определение наличия заданного
# элемента в списке list_=[2,8,3,4,3,5,2,1,0,3,4,4,5,8,7,7,5]
# Если элемент не найден, то выводится соответствующее сообщение

list_ = [2, 8, 3, 4, 3, 5, 2, 1, 0, 3, 4, 4, 5, 8, 7, 7, 5]
user_input = int(input('please enter any digit'))
if user_input not in list_:
    print(f'No such number: {user_input}')
else:
    print(f'{user_input} is in the list')

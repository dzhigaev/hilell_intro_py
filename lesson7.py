# Задан некоторый список A содержащий целые числа.
# Pазработать программу, которая вычисляет сумму элементов списка.
A = [1, 3, 4, 10, 9000, 100]
result = 0
b = A[:]
while b:
    result = b.pop() + result
print(result)

# Задан список строк. В каждой строке подсчитать количество вхождений заданного символа
list_of_strings = ["asdfg", "12345", "Hello", "world", "random string"]
given_symbol = "r"
index = 0
result = 0
while index < len(list_of_strings):
    print(index)
    result = list_of_strings[index].count(given_symbol)
    print(f"in \"{list_of_strings[index]}\": giver string was found {result} times")
    index += 1

# Пользователь вводит число. Определение наличия заданного
# элемента в списке list_=[2,8,3,4,3,5,2,1,0,3,4,4,5,8,7,7,5]
# Если элемент не найден, то выводится соответствующее сообщение

list_ = [2, 8, 3, 4, 3, 5, 2, 1, 0, 3, 4, 4, 5, 8, 7, 7, 5]
user_input = int(input("please enter any digit"))
if user_input not in list_:
    print(f"No such number: {user_input}")
else:
    print(f"{user_input} is in the list")

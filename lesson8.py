# 1.Заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице;
my_list = []
for number in range(100):
    if number == 0:
        my_list.append(1)
    elif number == 99:
        my_list.append(1)
    else:
        my_list.append(0)
print(my_list)

# 2.Сформировать возрастающий список из чётных чисел (количество элементов 45);.
my_list1 = []
for number1 in range(90):
    if number1 % 2 == 0:
        my_list1.append(number1)
print(my_list1)
print(len(my_list1))

# 3. Пользователь вводит число. Определить, содержит ли список данное число x. Вивести информационное сообщение
# содержит или не содержит ;
user_input = int(input('please enter number for checking'))
if user_input not in my_list1:
    print(f'No such number: {user_input}')
else:
    print(f'{user_input} is in the list')

# 4. Найдите сумму и произведение элементов списка. Результаты вывести на экран;
my_list2 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]

addition = 0
multiplication = 1
for element in my_list2:
    addition = addition + element
    multiplication *= element
print(addition)
print(multiplication)

# 5.Найти наибольший элемент списка и вывести его на экран;
print(max(my_list2))

# 6.Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран это значение;
my_list3 = [1, 1, 2, 3, 10, 10, 12, 14, 14]
for element in my_list3:
    if my_list3.count(element) > 1:
        print(element)

# 7.Поменять местами самый большой и самый маленький элементы списка;
my_list4 = [1, 20, 30, 2, 4, 5, 100, 30, 23]
maximum = max(my_list4)
minimum = min(my_list4)
for i in range(len(my_list4)):
    if my_list4[i] == maximum:
        my_list4[i] = minimum
    elif my_list4[i] == minimum:
        my_list4[i] = maximum

print(my_list4)

# 8. Дан произвольный список. Представьте его в обратном порядке.
random_list = [1, 3, 10, 'hello', 15, 'world', 'i am stuck in this list', 'help me']
reversed_list = random_list[::-1]
print(reversed_list)

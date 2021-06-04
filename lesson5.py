from math import sqrt

# задача1
# Из двух случайных чисел, одно из которых четное, а другое нечетное, определить и вывести на экран нечетное число.
first_num = int(input("enter any number"))
second_num = int(input("enter any number"))
if first_num % 2 == 0:
    print(first_num)
if second_num % 2 == 0:
    print(second_num)

# задача2
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# вариант без if
first_num = int(input("enter any number"))
second_num = int(input("enter any number"))
third_num = int(input("enter any number"))
list_of_nums = [first_num, second_num, third_num]
list_of_nums.sort()
print("middle number: ", list_of_nums[1])

# вариант с if
if second_num < first_num < third_num or third_num < first_num < second_num:
    print('middle number: ', first_num)
elif first_num < second_num < third_num or third_num < second_num < first_num:
    print('middle number: ', second_num)
else:
    print('middle number: ', third_num)

# задача3
# Вводятся координаты (x;y) точки и радиус круга (r). Определить принадлежит ли данная точка кругу, если его центр
# находится в начале координат.
x = float(input("x="))
y = float(input("y="))
r = float(input("r="))
h = sqrt(x ** 2 + y ** 2)
if h > r:
    print("точка находится за пределами круга")
else:
    print("точка принадлежит кругу")


# задача4
# Дана следующая функция y=f(x):
# y=2x-10, если x>0
# y = 0, если x = 0
# y = 2 * |x| - 1, если x < 0
# Требуется найти значение функции по переданному x.
def my_function(x):
    if x > 0:
        return 2*x - 10
    if x < 0:
        return 2*abs(x) - 1
    if x == 0:
        return 0


print(my_function(0))


# задача5
# Вводятся три целых числа. Определить какое из них наибольшее.
one = int(input("enter any number "))
two = int(input("enter any number "))
three = int(input("enter any number "))

maximum = one
if maximum < two:
    maximum = two
if maximum < three:
    maximum = three

print(maximum)

# задача6
# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.
one = int(input("one = "))
two = int(input("two = "))
three = int(input("three = "))
if one + two <= three or one + three <= two or two + three <= one:
    print("Треугольник не существует")
elif one != two and one != three and two != three:
    print("Разносторонний")
elif one == two == three:
    print("Равносторонний")
else:
    print("Равнобедренный")


# задача7
# Определить четверть координатной плоскости, которой принадлежит точка. Координаты точки ввести с клавиатуры.
x = int(input("x="))
y = int(input("y="))
if (x > 0) and (y > 0):
    print('I')
elif (x < 0) and (y > 0):
    print('II')
elif (x < 0) and (y < 0):
    print('III')
elif (x > 0) and (y < 0):
    print('IV')

# задача8
# Вводятся два целых числа. Проверить делится ли первое на второе. Вывести на экран сообщение об этом,
# а также остаток (если он есть) и частное (в любом случае).
a = int(input())
b = int(input())
if a % b == 0:
    print(f"{a} делится на {b}")
else:
    print(f"{a} не делится на {b}")
    print(f"Остаток: {(a % b)}")
print(f"Частное: {(a//b)}")

# задача9
# Найти корни квадратного уравнения и вывести их на экран, если они есть. Если корней нет, то вывести сообщение об
# этом. Конкретное квадратное уравнение определяется коэффициентами a, b, c, которые вводит пользователь.
print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)
if discr > 0:
    x1 = (-b + sqrt(discr)) / (2 * a)
    x2 = (-b - sqrt(discr)) / (2 * a)
    print(f"x1 = {x1} \nx2 = {x2}")
elif discr == 0:
    x = -b / (2 * a)
    print(f"x = {x}")
else:
    print("Корней нет")

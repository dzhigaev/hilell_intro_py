def main():
    # #Задача 1 Проработать встроенние функции множеств. Встроенние функции можно взять на сайте (
    # https://www.programiz.com/python-programming/set). Но на єтом сайте приведени примери для списков,
    # Задача переделать примери для множеств.
    my_set = {'1', 1, 10, 0.3, None}
    my_set.add(3)
    my_set.update(('10', 10000))
    my_set.remove('1')
    my_set.discard('1')
    my_set.pop()
    my_set.clear()
    my_set = {'1', 1, 10, 0.3, None}
    my_set_1 = {'1', 3, 10, 0.4, True}
    print(my_set | my_set_1)
    my_set.union(my_set_1)
    my_set_1.union(my_set)
    print(my_set & my_set_1)
    my_set.intersection(my_set_1)
    print(my_set - my_set_1)
    print(my_set_1 - my_set)
    my_set.difference(my_set_1)
    my_set_1.difference(my_set)
    print(my_set ^ my_set_1)
    my_set.symmetric_difference(my_set_1)
    my_set.symmetric_difference_update(my_set_1)
    my_set.union(my_set_1)
    my_set.update(my_set_1)
    print(my_set)

    # Задача 2
    # Дано три множества
    # set1 = {1, 2, 3, 4}
    # set2 = {2, 3, 5, 6}
    # set3 = {3, 4, 6, 7}
    # Одним действием (одной строкой) виполнить intersection єтих множеств
    set1 = {1, 2, 3, 4}
    set2 = {2, 3, 5, 6}
    set3 = {3, 4, 6, 7}
    intersection = set1 & set2 & set3
    print(intersection)

    # Задача 3
    # Дано три множества
    # set1 = {1, 2, 3, 4}
    # set2 = {2, 3, 5, 6}
    # set3 = {3, 4, 6, 7}
    # Одним действием (одной строкой) виполнить difference єтих множеств
    set1 = {1, 2, 3, 4}
    set2 = {2, 3, 5, 6}
    set3 = {3, 4, 6, 7}
    difference = set1 - set2 - set3
    print(difference)

    # Задача 4
    # Дано три множества
    # set1 = {1, 2, 3, 4}
    # set2 = {2, 3, 5, 6}
    # set3 = {3, 4, 6, 7}
    # Одним действием (одной строкой) виполнить union єтих множеств
    set1 = {1, 2, 3, 4}
    set2 = {2, 3, 5, 6}
    set3 = {3, 4, 6, 7}
    union = set1 | set2 | set3
    print(union)

    # Задача 5
    # Добавить список элементов к заданному набору
    sampleSet = {"Yellow", "Orange", "Black"}
    sampleList = ["Blue", "Green", "Red"]
    sampleSet.update(sampleList)
    print(sampleSet)

    # Задача 6
    # Вернуть новый набор идентичных предметов из заданных двух наборов
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    identic_1 = set1 & set2
    print(identic_1)

    # Задача 7
    # Возвращает новый набор со всеми элементами из обоих наборов, удаляя дубликаты.
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    combine = set1 | set2
    print(combine)

    # Задача 8 Учитывая два набора Python, обновите первый набор элементами, которые существуют только в первом наборе,
    # но не во втором наборе.
    set1 = {10, 20, 30}
    set2 = {20, 40, 50}
    set1.difference_update(set2)
    print(set1)

    # Задача 9
    # Удалите єлементи 10, 20, 30 из следующего набора
    set1 = {10, 20, 30, 40, 50}
    set1.remove(10)
    set1.remove(20)
    set1.remove(30)
    print(set1)

    # Задача 11
    # Проверьте, есть ли в двух наборах какие-либо общие элементы. Если да, отобразите общие элементы.
    set1 = {10, 20, 30, 40, 50}
    set2 = {60, 70, 80, 90, 10}
    print(set1 & set2)

    # Задача 12
    # Обновите набор 1, добавив элементы из набора 2
    set1 = {10, 20, 30, 40, 50}
    set2 = {60, 70, 80, 90, 10}
    set1.update(set2)
    print(set1)

    # Задача 13
    # Удалите элементы из set1, которые не являются общими для set1 и set2
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set1.intersection_update(set2)
    print(set1)


if __name__ == '__main__':
    main()

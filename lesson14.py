import datetime


def work_time(func):
    def wrapper(nums):
        start = datetime.datetime.now()
        func(nums)
        print(datetime.datetime.now() - start)

    return wrapper


@work_time
def squares(n):
    result = []
    start = 1
    for sq in range(n):
        my_dict = {x: x ** 2 for x in range(start)}
        result.append(my_dict)
        start += 1
    print(result)


def main():
    # squares(10)
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    list_3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    # first task
    list_1 = list(filter(lambda x: x % 2, list_1))
    list_3 = list(filter(lambda x: x % 2, list_3))
    # second task
    list_2 = list(filter(lambda x: x % 2 != 0, list_2))
    print(list_1)
    print(list_3)
    print(list_2)
    # third task
    list_4 = list(zip(list_1, list_2, list_3))
    print(list_4)
    # fourth task
    list_5 = list(map(sum, list_4))
    print(list_5)
    # fifth task
    list_5 = list(filter(lambda x: x % 2 != 0, list_5))
    print(list_5)


if __name__ == '__main__':
    main()

import json


def some_func(*args, **kwargs):
    length = len(kwargs)
    new_list = []
    for i in range(0, len(args), int(len(args) / length)):
        new_list.append(args[i:i + int(len(args) / length)])

    my_dict = dict(zip(kwargs.values(), new_list))
    return my_dict


def load_dict(some_dict, json_path):
    with open(f'{json_path}\json.json', 'w') as file:
        file.write(json.dumps(some_dict))


def main():
    result_for_eriting = some_func(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                   key1='key1', key2='key2', key3='key3', key4='key4', key5='key5')
    load_dict(result_for_eriting, r'D:\python\proj\homework\hilell_intro_py-dev')


if __name__ == '__main__':
    main()

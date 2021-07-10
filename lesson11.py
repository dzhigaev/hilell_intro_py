import json


def type_counter(your_dict):
    """
    This function checks which key has what value in given dictionary.
    """
    result_dict = {
        'int': [],
        'string': [],
        'float': [],
        'none_type': [],
        'bool': []
    }
    for k, v in your_dict.items():
        if isinstance(v, str):
            result_dict['string'].append(k)
        if isinstance(v, int):
            result_dict['int'].append(k)
        if isinstance(v, float):
            result_dict['float'].append(k)
        if isinstance(v, type(None)):
            result_dict['none_type'].append(k)
        if isinstance(v, bool):
            result_dict['bool'].append(k)
    return result_dict


def updating_hw_result():
    """
    This function takes JSON object from HW.json, changes it and rewrites to HW_result.json.
    """
    with open('HW.json', 'r') as given_json:
        incoming_json = json.loads(given_json.read())
    result_for_dumping = {'employee': {}}
    for id_ in incoming_json['employee']:
        name = f'''{id_['firstName']} {id_['lastName']}'''
        result_for_dumping['employee'].update({name: type_counter(id_)})
    back_to_json = json.dumps(result_for_dumping)
    with open('HW_result.json', 'w') as new_json:
        new_json.write(back_to_json+'\n')


if __name__ == "__main__":
    updating_hw_result()

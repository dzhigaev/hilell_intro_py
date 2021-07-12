import json


class MyJsonFormatter:
    def __init__(self,
                 default_path='C:',
                 result_path='C:'
                 ):
        self.result_for_dumping = {'employee': {}}
        self.default_path = default_path
        self.result_path = result_path
        self.update_HW_result()

    def grab_given_json(self):
        with open(f'{self.default_path}\HW.json', 'r') as file:
            self.given_json = json.loads(file.read())
        return self.given_json

    def reformat_given_json(self):
        for id_ in self.grab_given_json()['employee']:
            name = f'''{id_['firstName']} {id_['lastName']}'''
            self.result_for_dumping['employee'].update({name: self._type_counter(id_)})
        return json.dumps(self.result_for_dumping)

    @staticmethod
    def _type_counter(given_dict):
        result_dict = {
            'int': [],
            'string': [],
            'float': [],
            'none_type': [],
            'bool': []
        }
        for k, v in given_dict.items():
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

    def update_HW_result(self):
        with open(f'''{self.result_path}\HW_result.json''', 'w') as new_json:
            new_json.write(self.reformat_given_json() + '\n')


if __name__ == '__main__':
    best_json_formatter = MyJsonFormatter()

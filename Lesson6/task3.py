import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    user_file = './users.csv'
    hobby_file = './hobby.csv'


    with open(user_file, "r", encoding="utf-8") as uf:
        user_file = uf.readlines()

    with open(hobby_file, "r", encoding="utf-8") as hf:
        hobby_file = hf.readlines()

    dict_in = {}
    for i in range(len(user_file)):
        dict_in[user_file[i]] = hobby_file[i]
    if len(user_file) < len(hobby_file):
        return 1
    else:

        return dict_in




dict_out = prepare_dataset('users.csv', 'hobby.csv')
print(dict_out)

with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
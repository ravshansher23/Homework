from pprint import pprint


def get_parse_attrs():
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""

    return list_out(string)

list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    while True:
        row = fr.readline()
        if not row:
            break
        row_split = row.split()
        addr = row_split[0]
        req_type = row_split[5]
        resource = row_split[6]
        list_out.extend([addr, req_type, resource])


pprint(list_out, width=40)


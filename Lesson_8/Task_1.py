import re


re_address = re.compile(r'(?P<username>[a-zA-Z0-9\.\-\_]+)@(?P<domain>[a-zA-Z0-9\.\-\_]+)')


def email_parse(email):

    try:
        addr = map(lambda x: x.groupdict(), re_address.finditer(email))
        print(*addr)
    except Exception as err:
        print(f'Ошибка: {err}')




email_parse('someone@geekbrains.ru')
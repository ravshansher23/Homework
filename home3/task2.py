def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    translate_dict = {'one': 'один',
                      'two': 'два',
                      'three': 'три',
                      'four': 'четыре',
                      'five': 'пять',
                      'six': 'шесть',
                      'seven': 'семь',
                      'eight': 'восемь',
                      'nine': 'девять',
                      'ten': 'десять',
                    'One': 'Один',
                    'Two': 'Два',
                    'Three': 'Три',
                    'Four': 'Четыре',
                    'Five': 'Пять',
                    'Six': 'Шесть',
                    'Seven': 'Семь',
                    'Eight': 'Восемь',
                    'Nine': 'Девять',
                    'Ten': 'Десять'

    }

    if value in translate_dict:

        str_out = translate_dict[value]
    else:
        str_out = None
    return str_out
print(num_translate("Ten"))
print(num_translate("eleven"))
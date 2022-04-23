
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


    }

    if value in translate_dict:

        str_out = translate_dict[value]
    else:
        str_out = None
    return str_out
print(num_translate("ten"))
print(num_translate("eleven"))
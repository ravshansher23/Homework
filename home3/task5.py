import random


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# def get_jokes(count: int) -> list:
#     """Возвращает список шуток в количестве count"""
#     random.shuffle(nouns)
#     random.shuffle(adverbs)
#     random.shuffle(adjectives)
#     list_in = zip(nouns, adverbs, adjectives)
#
#     for i in list_in:
#         list_out = list(i)
#         if list(i) in list_out:
#             list_in.pop(list(i))
#         else:
#             list_out = list(i)
#
#     return list_out
# print(get_jokes(2))
# print(get_jokes(10))




def get_jokes_adv() -> dict:
    random.shuffle(nouns)
    random.shuffle(adverbs)
    random.shuffle(adjectives)


    for i in range(len(nouns)):
        dict_1 = {nouns[i]: {adverbs[i], adjectives[i]}}
        print(f'Шутка №', (i + 1), dict_1)



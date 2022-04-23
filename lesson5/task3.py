tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    len_klas = len(klasses)


    return ((tut, klasses[i]) if i < len_klas else (tut, None)
        for i, tut in enumerate(tutors))



generator = check_gen(tutors, klasses)
print(type(generator))# добавьте здесь доказательство, что создали именно генератор
for _ in range(len(tutors)):
    print(next(generator))
#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
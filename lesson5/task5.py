src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

def get_uniq_numbers(*argv):

    src_set = set()

    for i in argv:
        if not i in src_set:
            src_set.add(i)
        else:
            src_set.remove(i)

    return [num for num in argv if num in src_set]

result = get_uniq_numbers(*src)
print(result)

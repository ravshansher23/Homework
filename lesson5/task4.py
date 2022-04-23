result = [12, 44, 4, 10, 78, 123]
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
def get_numbers(src):

    result_gen = [num for i, num in enumerate(src) if i > 0 and src[i] > src[i - 1]]

    print(result_gen)

    return result_gen

print(*get_numbers(src))
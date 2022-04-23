def thesaurus(*args) -> dict:
    dict_out = {}
    dict_in = {}
    list_out = []
    for i in args:

        dict_out[i[0]] = [i]
        if dict_in.get(i[0]) == None:

            dict_in[i[0]] = i.split()
        else:
            list_out = dict_in.get(i[0])
            list_out.append(i)
            dict_in[i[0]] = list_out


    return dict_in

    # пишите свою реализацию здесь


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Петя"))
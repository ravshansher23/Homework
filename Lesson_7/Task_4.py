import os
stat_data = {}
len_100 = []
len_1000 = []
len_10000 = []
len_100000 = []
dir_d = os.path.dirname(os.path.abspath(__file__))
some_data = os.path.join(dir_d, 'some_data')

for file in os.scandir(some_data):

    if os.stat(file).st_size < 100:
        len_100.append(file)
    elif 1000 >= os.stat(file).st_size >= 100:
        len_1000.append(file)
    elif 1000 < os.stat(file).st_size < 10000:
        len_10000.append(file)
    else:
        len_100000.append(file)

stat_data.setdefault(100, len(len_100))
stat_data.setdefault(1000, len(len_1000))
stat_data.setdefault(10000, len(len_10000))
stat_data.setdefault(100000, len(len_100000))
print(stat_data)

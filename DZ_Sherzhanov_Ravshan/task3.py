
number = None
def transform_string(number):


    if (n % 10 == 1) and n != 11:
        number = list[n, 'процент']
    elif (n % 10 >= 2) and (n % 10 <=4) and n != 12 and n != 13 and n != 14:
        number = list[n, 'процента']
    else:
        number = list[n, 'процентов']
    return number

for n in range(1, 101):
    print(transform_string(n))


time = int(input('Введите кол-во сек: '))

if time < 0:
    print('Время не может быть отрицательным')
else:
    def convert_time(time: list)-> str:

        day = time // (24 * 60 * 60)
        hours = (time - (day * 24 * 60 * 60)) // 3600
        minutes = (time - (day * 24 * 60 * 60) - (hours * 60 * 60)) // 60
        seconds = (time - (day * 24 * 60 * 60) - (hours * 60 * 60) - (minutes * 60))
        if day > 0:

            time = [day, 'д', hours, 'ч', minutes, 'м', seconds, 'с']
        elif hours > 0:
            time = [hours, 'ч', minutes, 'м', seconds, 'с']
        elif minutes > 0:
            time = [minutes, 'м', seconds, 'с']
        else:
            time = [seconds, 'с']
        return time




    result = convert_time(time)
    print(result)






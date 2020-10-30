
time_in_second = int(input('Введите время в секундах \n'))

hours = int(time_in_second / (60 * 60))
minuts = int((time_in_second - hours * 60 * 60) / 60)
seconds = int(time_in_second- hours * 60 * 60 - minuts * 60)

print(hours,':',minuts,':',seconds)


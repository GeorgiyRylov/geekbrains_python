distance = int(input('Введите дистанцию с которой вы начинаете \n'))
distance_wish = int(input('Введите дистанцию к которой вы стремитесь \n'))
count_day = 1
while distance < distance_wish:
    distance *= 1.1
    #print(distance)
    count_day += 1
print(count_day)


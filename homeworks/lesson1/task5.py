proceeds = int(input('Введите сумму выручки \n'))
costs = int(input('Введите сумму издержак \n'))

gain = proceeds - costs

if gain > 0:
    difference = round(proceeds / costs, 2)
    print('Прибыль:', gain, '\nРентабельность составляет', difference)
    personal_count = int(input('Введите количество сотрудников  \n'))
    gain_of_person = round(gain / personal_count, 2)
    print('Прибыль на 1 человека составляет', gain_of_person)
else:
    print('Убыток',gain)
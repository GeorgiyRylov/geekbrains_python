
number = int(input('Введите число целое положительное число \n'))

result = 0
while number and result != 9:
    temp = number % 10
    if temp > result:
        result = temp
    number //=10

print(result)

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Enter the number: '))
k = 0
while 2 ** k < n:
    print(2 ** k, end=' ')
    k += 1
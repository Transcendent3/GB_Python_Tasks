# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
from random import randint
n = int(input('Enter the number of array elements: '))
a = list()
for i in range(n):
    a.append(randint(1, 10))
print(a)
x = int(input('Enter the number to be found in the array: '))
if x in a:
    print(x)
else:
    min_x = abs(a[0] - x)
    pos = 0
    for i in range(1, n):
        difference = abs(a[i] - x)
        if difference == min_x:
            pos = pos if a[pos] < a[i] else i
        elif difference < min_x:
            min_x = difference
            pos = i
    print(a[pos])

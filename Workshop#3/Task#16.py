# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3 -> 1
import random
from random import randint
n = int(input('Enter the number of array elements: '))
a = list()
for i in range(n):
    a.append(randint(1, 10))
print(a)
x = int(input('Enter the number to be found in the array: '))
print(a.count(x))
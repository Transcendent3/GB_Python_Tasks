# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

def sum_1(a, b): #решение к условию задачи
    if a == 0:
        return b
    return sum_1(a - 1, b + 1)


# def sum_1(a, b): #не получилось доделать решение для отрицательных чисел
#     if a < 0 and b < 0:
#         if a == -1:
#             return b - 1
#         return sum_1(a + 1, b - 1)
#     elif a < 0 and b > 0:
#         if a == -1:
#             return b - 1
#         return sum_1(a + 1, b - 1)
#     elif a > 0 and b < 0:
#         if b == -1:
#             return a - 1
#         return sum_1(a - 1, b + 1)
#     else:
#         if a == 0:
#             return b
#         return sum_1(a - 1, b + 1)




print(sum_1(int(input()),int(input())))
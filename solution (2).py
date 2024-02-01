#coding: utf-8
low = int(input())      # нижняя граница
high = int(input())     # верхняя граница
between = True          # пока все числа в интервале

while line := input():  # вводить до первой пустой строки
    # обновить флаг если нужно
    if between:
        between = low <= int(line) <= high

print(between)
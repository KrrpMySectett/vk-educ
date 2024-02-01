#coding: utf-8
n = int(input())
max_values = []
for _ in range(n):
    record = input()
    values = record.split()
    values = [int(value) for value in values]
    max_value = max(values)
    max_values.append(max_value)
max_values.sort(reverse=True)
output = ';'.join(map(str, max_values))
print(output)
s = input()
n = s.split()
c1 = len(n)
c2 = 0
for _ in n:
    c2 += len(_)
print(c2/c1)
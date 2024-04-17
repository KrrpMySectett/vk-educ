def g():
   b = int(input())
   def h():
       nonlocal b
       b += 10
   h()
   print(b)
g()
class Counter:

   def __init__(self, initial_count):
       self.count = initial_count

   def increment(self):
       self.count += 1
      
   def get(self):
       return self.count


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
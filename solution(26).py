class Person:
   def __init__(self, age):
       self._age = age

   @property
   def age(self):
       return self._age

   @age.setter
   def age(self, value):
       if value < 0:
           self._age = 0
       else:
           self._age = value
      

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
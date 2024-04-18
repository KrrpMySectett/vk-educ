class ContextDictionary:
   def __init__(self):
       self.dictionary = None

   def __enter__(self):
       self.dictionary = {}
       return self.dictionary

   def __exit__(self, exc_type, exc_val, exc_tb):
       self.dictionary = None

   def put(self, key, value):
       self.dictionary[key] = value

   def get(self, key):
       return self.dictionary[key]

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
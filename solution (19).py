def repeat_deco(n=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
@repeat_deco(4)
def hello():
    print ("hello")

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
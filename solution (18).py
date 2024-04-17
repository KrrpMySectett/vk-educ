def cache_deco(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
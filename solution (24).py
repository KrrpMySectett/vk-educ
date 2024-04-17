def cache_deco(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

def solution(func_map, func_filter, data):
    filtered_data = filter(func_filter, data)
    mapped_data = map(func_map, filtered_data)
    for i, data in enumerate(mapped_data):
        if i % 2 == 0:
            yield data

code = []
while data := input():
  code.append(data)
code = "\n".join(code)
exec(code)
from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
    queue = deque(nums)
    for _ in range(n):
        last_element = queue.pop()
        queue.appendleft(last_element)
    return list(queue)

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
"""
https://www.codewars.com/kata/529adbf7533b761c560004e5/train/python
"""


def fibonacci(n, last=1, cache={0: 0, 1: 1}):
    if n in cache:
        return cache[n]
    else:
        cache[last + 1] = cache[last - 1] + cache[last]
        return fibonacci(n, last + 1, cache)


assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5

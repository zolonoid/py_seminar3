from random import randint
from itertools import zip_longest

print("Найти произведение пар чисел списка.")
try:
    nums = [randint(1, 9) for i in range(randint(4, 9))]
    print(f"Задан список: {nums}")
    l = len(nums)
    totalPairs = l-(l >> 1)
    firstHalf = range(0, totalPairs)
    lastHalf = range(l-1, l-1-totalPairs, -1)
    res = [nums[i]*nums[k] for i, k in zip_longest(firstHalf, lastHalf)]
    print(f"Произведения пар чисел: {res}")
except Exception as exc:
    print(f"Что-то пошло не так...\n{exc}")

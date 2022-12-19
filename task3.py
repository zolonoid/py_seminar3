from random import uniform, randint
from math import floor
from itertools import zip_longest

print("найти разницу между максимальным и минимальным значением дробной части элементов.")
try:
    nums = [round(uniform(0, 10),2) for i in range(randint(4, 9))]
    print(f"Задан список: {nums}")
    floors=[floor(x) for x in nums]
    decimals=[round(n-f,2) for n,f in zip_longest(nums, floors)]
    print(f"Разница между max и min значением дробной части: {max(decimals)-min(decimals):.2f}")
except Exception as exc:
    print(f"Что-то пошло не так...\n{exc}")
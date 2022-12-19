from random import randint

print("Найти сумму элементов списка, стоящих на нечетной позиции.")
try:
    nums = list(randint(1, 9) for i in range(5))
    print(f"Задан список: {nums}")
    result = 0
    for pos in range(1, len(nums), 2):
        result += nums[pos]
    print(f"Сумма элементов равна {result}")
except:
    print("Что-то пошло не так...")

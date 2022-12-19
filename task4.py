
print("Преобразовать десятичное число в двоичное.")
inp = input("Введите целое десятичное число...\n")
try:
    value = int(inp)
    print(f"{value} -> {value:b}")
except:
    print("Это не целое число")
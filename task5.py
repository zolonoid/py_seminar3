# Получить список чисел Фибоначчи для k
def FiboPosNeg(k):
    if (k < 2):
        raise ValueError
    pF = [0, 1]
    nF = [0, 1]
    for n in range(2, k+1):
        pF.append(pF[n-1]+pF[n-2])
        nF.append(nF[n-2]-nF[n-1])
    del nF[0]
    nF.reverse()
    return nF+pF


print("Составить последовательность Фибоначчи на основе указанного числа.")
inp = input("Введите целое положитльное число k ...\n")
try:
    k = int(inp)
    print(FiboPosNeg(k))
except:
    print("Это непраильное число")

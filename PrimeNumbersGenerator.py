from random import choice

def GetPrimeNmbr(a, b):
    if a<=3:
        yield 2, 3
        a = 4
    for i in range(a, b+1):
        for k in range(2, int(i**(1/2))+1):
            if i%k == 0:
                break
        if k == int(i**(1/2)) and i%k!=0:
            yield i

Transform = lambda arr: [min([abs(arr[0]), abs(arr[1])]), max([abs(arr[0]), abs(arr[1])])]

n, m = int(input("Отрезок, на котором расположено множество простых чисел: ")), int(input())

n, m = Transform([n, m])

PrimeNmbr = [i for i in GetPrimeNmbr(n, m)]

if len(PrimeNmbr)!=0:
    print("Сгенерированное простое число: %d" % choice(PrimeNmbr))
else:
    print("На заданном отрезке простых чисел не найдено.")

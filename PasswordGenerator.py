from random import randrange

GenPassword = lambda n: "".join([chr(randrange(33, 127)) for i in range(n)])

k = int(input("Количество символов в пароле: "))

print("Сгенерированный пароль: %s" % GenPassword(k))

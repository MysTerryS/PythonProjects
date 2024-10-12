def GetHystogram(word):
    Letters = list({str(i) for i in word})
    for i in Letters:
        print("{}: {:|>{}} {:.1%}".format(i, "|", word.count(i), word.count(i)/len(word)))

s = input("Введите любую строку: ")
print("Гистограмма введенной строки: ")
GetHystogram(s)

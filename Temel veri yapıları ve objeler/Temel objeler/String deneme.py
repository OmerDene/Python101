"""mys = {"omer","mehmet","sss"}
print(type(mys))
mys.remove("omer")
mys.add("huseyin")
print(mys)

sozluk = {"omer": 2,"ahmet": 5,"ozkan" : 4 ,"eymen":7}
print(sozluk.values())
print(sozluk.keys())
print(sozluk.items())

a = "17"
print(len(a))
b = 19
print(type(b))
"""






def toplama(*parametreler): # Artık parametreler değişkenini bir demet gibi kullanabilirim.
    toplam =  0
    for i in parametreler:
        toplam += i
    return toplam
print(toplama(3,444,44,4,4,4,4,4,4,4,4,4))
   





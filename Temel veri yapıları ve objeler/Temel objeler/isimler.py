isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisim = ["hhhh","zzz","ddd","tttt","ccc","aaa","bbb"]

liste = list(zip(isim,soyisim))

liste.sort()

for i,j in liste:
    print(i,j)
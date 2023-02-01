sayı = []
harf = []

a = input("Metin ya da sayı giriniz: ")

for i in a:
    if i.isalpha():
        harf.append(i)

    elif i.isnumeric():
        sayı.append(i)

print("Sayılar:", sayı,"\nHarfler:", harf)










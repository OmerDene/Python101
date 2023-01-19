toplam = 0
while True:
    sayı = input("sayı giriniz")
    if (sayı == "q"):
        break
    sayı = int(sayı)

    toplam += sayı
print("sayınız",toplam)

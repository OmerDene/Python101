print("""Atm makinesi işlemleri
Bakiye sorgulama için 1 i
Para yatırma için 2 yi
Para çekme için 3 ü
programdan çıkmak için 'q' ya basınız.

Seçiniz
""")
bakiye = 1000

while True :
    islem = input("işlemi seciniz :")
    if(islem == "1"):
        print("Bakiyeniz :" ,bakiye)
    elif(islem == "2"):
         miktar = int(input("Para yatırıyorsunuz... :"))
         print("Mevcut bakiye :", bakiye)
         bakiye += miktar
    elif(islem=="3"):
        miktar = int(input("Para çekiyorsunuz... :"))
        if(bakiye - miktar< 0):
            print("yetersiz bakiye")
            continue
        bakiye -= miktar
        print("Mevcut bakiye :" ,bakiye)
    elif(islem == "q"):
        print("Yine bekleriz")
    else:
        print("Geçersiz işlem")






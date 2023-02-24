print("Hesap makinesi")

while True:
    islem = input("işlemi seciniz: ")

    if (islem == "q") :
        print("Çıkıs yapılıyor...")
        break
    elif(islem == "+" ):
        sayı1= int(input("ilk sayıyı giriniz :"))
        sayı2 = int(input("ikinci sayıyı giriniz :"))
        sonuc = sayı1+sayı2
        print("Toplama işleminizin sonucu: ",sonuc)
    elif (islem == "-"):
        sayı1 = int(input("ilk sayıyı giriniz :"))
        sayı2 = int(input("ikinci sayıyı giriniz :"))
        sonuc = sayı1 - sayı2
        print("Çıkarma işleminizin sonucu: ", sonuc)
    elif (islem == "/"):
        sayı1 = int(input("ilk sayıyı giriniz :"))
        sayı2 = int(input("ikinci sayıyı giriniz :"))
        sonuc = sayı1 / sayı2
        print("Bölme işleminizin sonucu: ", sonuc)
    elif (islem == "*"):
        sayı1 = int(input("ilk sayıyı giriniz :"))
        sayı2 = int(input("ikinci sayıyı giriniz :"))
        sonuc = sayı1 * sayı2
        print("Çarpma işleminizin sonucu: ", sonuc)
    else:
        print("Geçersiz işlem")
        continue






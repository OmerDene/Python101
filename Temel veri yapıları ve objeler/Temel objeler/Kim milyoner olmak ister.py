import random
liste = ["Kevser Hanım","Murat Bey","Özkan Bey","Ömer Bey"]
secim = random.choice(liste)
while True:
    print("KİM MİLYONER OLMAK İSTER YARIŞMASI ")
    print("Yarışmacımız {} geliyor.. Alkış lütfen..." .format(secim))
    Secenek1 = "a"
    Secenek2 = "b"
    Secenek3 = "c"
    Secenek4 = "d"
    evet = "evet"
    hayır = "hayır"
    jokerhakkı = 1
    print("Türkiyenin başkenti neresidir  ?","A : Konya", "B : Adıyaman" , "C : Ankara","D : İstanbul", sep ="\n" )
    cevap2 = input("Joker kullanmak ister misiniz : ")
    if (cevap2 == "evet"):
        jokerhakkı -= 1
        print("Seyirciye soruluyor...", "Cevap A : %27", "Cevap B : %15", "Cevap C : %52", "Cevap D : %6", sep="\n")
    elif (cevap2 == "hayır"):
        print("Cevap veriliyor.. ")

    cevap1 = input("Şıkkı seçiniz :")

    if(cevap1 == Secenek1 ):
        print("Elendiniz")
        break
    elif(cevap1 == Secenek2):
        print("Elendiniz")
        break
    elif(cevap1 == Secenek3):
        print("Tebrikler!")

    elif(cevap1 == Secenek4):
        print("Elendiniz")
        break


    print("Avrupanın en büyük toprak ölçüsüne sahip ülkesi hangisidir ? ", "A : Rusya", "B : Almanya",
              "C : Hırvatistan", "D : Belçika", sep="\n")
    cevap2 = input("Joker kullanmak ister misiniz : ")
    if (cevap2 == "evet" and jokerhakkı !=0):
            print("Seyirciye soruluyor...", "Cevap A : %52", "Cevap B : %27", "Cevap C : %15", "Cevap D : %6", sep="\n")
            jokerhakkı -= 1
    elif (cevap2 == "hayır"):
            print("Cevap veriliyor.. ")
    elif(jokerhakkı==0 and cevap2=="evet"):
            print("Seyirci jokeriniz kalmamıştır...")


    cevap1 = input("Şıkkı seçiniz :")
    if (cevap1 == Secenek1):
            print("Tebrikler!")

    elif (cevap1 == Secenek2):
            print("Elendiniz")
            break
    elif (cevap1 == Secenek3):
            print("Elendiniz!")
            break
    elif (cevap1 == Secenek4):
            print("Elendiniz")
            break


    print("Dünyanın uydusu hangisidir ? ", "A : Ay", "B : jupiter",
          "C : Başakşehir", "D : Satürn", sep="\n")
    cevap2 = input("Joker kullanmak ister misiniz : ")
    if (cevap2 == "evet" and jokerhakkı != 0):
        print("Seyirciye soruluyor...", "Cevap A : %52", "Cevap B : %27", "Cevap C : %15", "Cevap D : %6", sep="\n")
    elif (cevap2 == "hayır"):
        print("Cevap veriliyor.. ")
    elif (jokerhakkı == 0):
        print("Seyirci jokeriniz kalmamıştır...")


    cevap1 = input("Şıkkı seçiniz :")
    if (cevap1 == Secenek1):
        print("Tebrikler!,Büyük Ödülü Kazandınız...")
        break
    elif (cevap1 == Secenek2):
        print("Elendiniz!")
        break
    elif (cevap1 == Secenek3):
        print("Elendiniz!")
        break
    elif (cevap1 == Secenek4):
        print("Elendiniz!")
        break
    else:
        break
        print("Yarışma sonlanmıştır")
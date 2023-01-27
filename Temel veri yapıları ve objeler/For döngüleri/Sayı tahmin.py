import random
import time
print("guess what... ")

sayımız = random.randint(1,2)
tahmin_hakkı = 7
while True:
    tahmin_sayısı = int(input("Tahmininizi giriniz: "))
    if(tahmin_sayısı<sayımız):
        print("Bilgiler kontrol ediliyor...")
        time.sleep(1)
        print("Sayımız tahmininizden yüksektir...")
        tahmin_hakkı -= 1
    elif(tahmin_sayısı>sayımız):
        print("Bilgiler kontrol ediliyor...")
        time.sleep(1)
        print("Sayımız tahmininizden düşüktür...")
        tahmin_hakkı -= 1
    elif(sayımız==tahmin_sayısı):
        print("Bilgiler kontrol ediliyor...")
        time.sleep(1)
        print("Tebrikler! ",sayımız)
        yeniden = input("Yeniden oynamak ister misiniz: ")
        if(yeniden=="evet" or yeniden == "EVET" or yeniden=="yes" or yeniden=="YES"):
            print("Eglence Devam Ediyor...")
            continue
        elif(yeniden=="hayır" or yeniden== "HAYIR" or yeniden=="no" or yeniden=="NO"):
            print("Yine Bekleriz...")
            break
        else:
            print("Geçersiz tuşlama yaptınız, çıkış yapılıyor...")
            break


    if (tahmin_hakkı == 0):
        print("Tahmin hakkınız dolmuştur...")
        break
















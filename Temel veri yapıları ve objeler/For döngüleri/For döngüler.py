
"""Liste = [4,5,6,7,8,9]

for omer in Liste:
    print("omercik",omer +1)

while True:
    isim = input("isim(q ya basarsanız çıkış yapılır) :")
    if(isim == "q"):
        print("cıkıs yapılmıstır")
        break

liste = [(1,3),(4,5),(6,7)]

liste1 = [i *j  for i,j in liste]
print(liste1)

print("Kullanıcı girisi programı")

user = "omer"
password = 12345

Giris_hakkı = 3

while True:
    userName = input("Kullanıcı adı giriniz :")
    userPassword = input("Kullanıcı passwordu giriniz :")
    if(user==userName and password!=userPassword):
        print("Parola hatalı ")
        Giris_hakkı -= 1
    elif(user!=userName and password==userPassword):
        print("Kullanıcı adı hatalı ")
        Giris_hakkı -= 1
    elif(user!=userName and password!=userPassword):
        print("Kullanıcı adı ve parola hatalı ")
        Giris_hakkı -= 1
    else:
        print("Sisteme basarı ile giris yapıldı")
        break
    if(Giris_hakkı==0):
        print("giris hakkınız kalmamıstır")
        break


"""
sys_kul_adı = "ilker"

sys_parola = "12345"

giriş_hakkı = 3
print("Toplam Giriş Hakkınız : {}".format(giriş_hakkı))

Cevap = input("Giriş yapmak isterseniz ’Giriş’ yazın Giriş yapmak istemezseniz ’Çıkış’ yazınız")
if (Cevap == "Giriş"):
    while True:
        kullanıcı_adı = input("Kullanıcı Adınız Giriniz : ")
        parola = input("Parolanızı Giriniz :")

        if (kullanıcı_adı != sys_kul_adı and parola == sys_parola):
            giriş_hakkı -= 1
            print(
                "Hatalı Kullanıcı adı\n Kalan Giriş hakkınız {} \n Kullanıcı adınızı mı Unuttunuz : Evet ya da Hayır".format(
                    giriş_hakkı))
            Cevap2 = input("Cevabı giriniz:")
            if Cevap2 == "evet":
                sys_kul_adı = input("Yeni Kullanıcı adınızı Giriniz: ")

            if (Cevap2 == "Hayır"):
                print("Programdan çıkış yapılıyor....")
                break

            else:
                print("Lütfen doğru yazdığınızdan emin olunuz")

        elif (kullanıcı_adı == sys_kul_adı and parola != sys_parola):
            giriş_hakkı -= 1

            print("Hatalı şifre\n Kalan Giriş hakkınız {} \n Şifrenizi mi Unuttunuz : Evet ya da Hayır".format(
                giriş_hakkı))
            Cevap3 = input("Cevabı giriniz:")

            if Cevap3 == "evet":
                sys_parola = input("Yeni şifrenizi Giriniz: ")

            elif (Cevap2 == "Hayır"):

                print("Programdan çıkış yapılıyor....")
                break

            else:
                print("Lütfen doğru yazdığınızdan emin olunuz")





        elif (kullanıcı_adı != sys_kul_adı and parola != sys_parola):

            giriş_hakkı -= 1

            print(
                "Hatalı şifre ve kullanıcı adı\n Kalan Giriş hakkınız {} \n Kullanıcı adınızı ve şifrenizi mi Unuttunuz : Evet ya da Hayır".format(
                    giriş_hakkı))

            Cevap4 = input("Cevabı giriniz:")

            if Cevap4 == "Evet":
                sys_parola = input("Yeni şifrenizi Giriniz: ")

                sys_kul_adı = input("Yeni Kullanıcı adınızı Giriniz: ")



        elif (kullanıcı_adı == sys_kul_adı and parola == sys_parola):

            print("Sisteme giriş yapılıyor....")
            break
elif (Cevap == "Çıkış" or "çıkış"):
    print("Çıkış yapılıyor")






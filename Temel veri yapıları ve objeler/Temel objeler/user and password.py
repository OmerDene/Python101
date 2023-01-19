print("Hesap giris bilgileri")

myName = "omer"
myPassword = "12345"

myNameGiris = input("Kullanıcı adı girin :")
myPasswordGiris = input("parola girin :")

if(myName == myNameGiris and myPassword !=myPasswordGiris) :
    print("parola hatalı")
elif(myName!=myNameGiris and myPassword==myPasswordGiris) :
    print("kullanıcı adı hatalı")
elif(myName!=myNameGiris and myPassword!=myPasswordGiris) :
    print("kullanıcı adı ve sifre hatalı")
else :
    print("sisteme basarıyla giris yapıldı")






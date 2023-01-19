print("""***********************************
Hesap makinesi programı

işlemler:

1.Toplama işlemi

2.Çıkarma işlemi

3.Çarpma işlemi

4.Bölme işlemi



*********************************""")

sayı_1 = int(input("ilk sayıyı giriniz :"))
sayı_2 = int(input("ikinci sayıyı giriniz :"))
işlem = input("işlemi giriniz :")

if(işlem == "1") :
    print("{} ile {} in toplamı {} dir".format(sayı_1,sayı_2,sayı_1+sayı_2))
elif(işlem == "2") :
    print("{} ile {} in çıkanı {} dir".format(sayı_1,sayı_2,sayı_1-sayı_2))
elif(işlem == "3") :
    print("{} ile {} in çarpımı {} dir".format(sayı_1,sayı_2,sayı_1*sayı_2))

elif(işlem == "4") :
    print("{} ile {} in bölümü {} dir".format(sayı_1,sayı_2,sayı_1/sayı_2))
else :
    print("geçersiz işlem")


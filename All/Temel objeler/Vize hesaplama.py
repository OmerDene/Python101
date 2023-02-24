Vize_1 = int(input("ilk vizenizi giriniz :"))
Vize_2 = int(input("ikinci vizenizi giriniz :"))
Final = int(input("finalinizi giriniz :"))

a = (Vize_1 *30 ) / 100
b = (Vize_2 *30 ) /100
c = (Final * 40) / 100
Ortalama = a + b +c
if(Ortalama>=90):
    print("AA")
elif(Ortalama>=85):
    print("BA")
elif(Ortalama>=80):
    print("BB")
elif(Ortalama>=75):
    print("BC")
elif(Ortalama>=70):
    print("CC")
elif(Ortalama>=65):
    print("DC")
elif(Ortalama>=60):
    print("DD")
else :
    print("FF")



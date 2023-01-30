import random

a =["Elazığ","Adıyaman","Sivas","Ankara"]
b =["Agrı","İzmir","Antalya","Ankara"]
c = ["Edirne","Yozgat", "İstanbul","Ankara"]




yanlısSecim = random.choice(a)
yanlısSecim2= random.choice(b)
yanlısSecim3= random.choice(c)
dogruCevap = "Ankara"




print("Aşagıdakilerden hangisi Türkiyenin başkentidir?\nA:{}\nB:{}\nC:{}\nD:{}\n ".format(yanlısSecim,yanlısSecim2,yanlısSecim3,dogruCevap))
""" Şıklar Geliyor...."""
cevap = input("Doğru şıkkı Seçiniz: ")
if(cevap ==dogruCevap):
    print("Tebrikler...")
elif(cevap == yanlısSecim or cevap == yanlısSecim2 or cevap==yanlısSecim3):
    print("Yanlıs Cevap...")






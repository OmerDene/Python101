#Maası 3000 bin tl den yüksek olanlara %10 zam
#Maası 3000 bin tl den az olanlara %20 zam

salaries = [2000,5000,4000,5000,6000]
new_salaries = []

for i in salaries:
    if(i>3000):
        y= int(i*10/100 + i)
        new_salaries.append(y)
        print(y)

for i in salaries:
    if(i<3000):
        y = int(i*20/100 + i)
        new_salaries.append(y)
        print(y)
"""
Alternatif hesaplama 


maaslar = [1000, 2000, 3000, 4000, 5000]

def zam_yap(maas):
    if maas >= 3000:  # Eğer maaş 3000'den büyük ve eşitse
        return (maas * 10 / 100) + maas  # %10 zam yap
    else:  # Değilse
        return (maas * 20 / 100) + maas  # %20 zam yap


for maas in maaslar:  # Maaşlar üzerine döngü uygula
    print(zam_yap(maas))  # zamlı maaşı ekrana yazdır
"""


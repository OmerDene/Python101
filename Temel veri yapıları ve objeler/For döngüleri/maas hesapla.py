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



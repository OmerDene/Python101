import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


"""
#populasyon =np.random.randint(0,10,10000)
#np.random.seed(100)
#orneklem = np.random.choice(a=populasyon,size=100)
#np.random.seed(10)

orneklem1 = np.random.choice(a = populasyon, size = 100)
orneklem2 = np.random.choice(a = populasyon, size = 100)
orneklem3 = np.random.choice(a = populasyon, size = 100)
orneklem4 = np.random.choice(a = populasyon, size = 100)
orneklem5 = np.random.choice(a = populasyon, size = 100)
orneklem6 = np.random.choice(a = populasyon, size = 100)
orneklem7 = np.random.choice(a = populasyon, size = 100)
orneklem8 = np.random.choice(a = populasyon, size = 100)
orneklem9 = np.random.choice(a = populasyon, size = 100)
orneklem10 = np.random.choice(a = populasyon, size = 100)
"""
#print((orneklem1.mean() + orneklem2.mean() + orneklem3.mean() + orneklem4.mean() + orneklem5.mean()
#+ orneklem6.mean() + orneklem7.mean() + orneklem8.mean() + orneklem9.mean() + orneklem10.mean() )  / 10)
"""
b = np.random.randint(1,10)
#print(b)
np.random.seed(10)
c = np.random.randint(1,10) ### bu satırda seed fonksiyonu ile rastgele seçilen değer hep aynı döner.
#print(c)
A = pd.DataFrame([30,27,21,27,29,30,20,20,27,32,35,22,24,23,25,27,23,27,23,
        25,21,18,24,26,33,26,27,28,19,25])

B = pd.DataFrame([37,39,31,31,34,38,30,36,29,28,38,28,37,37,30,32,31,31,27,
        32,33,33,33,31,32,33,26,32,33,29])


A_B = pd.concat([A,B],axis=1)
A_B.columns = ["A","B"]
#print(A_B.head())
A = pd.DataFrame([30,27,21,27,29,30,20,20,27,32,35,22,24,23,25,27,23,27,23,
        25,21,18,24,26,33,26,27,28,19,25])

B = pd.DataFrame([37,39,31,31,34,38,30,36,29,28,38,28,37,37,30,32,31,31,27,
        32,33,33,33,31,32,33,26,32,33,29])

#A ve A'nın grubu
GRUP_A = np.arange(len(A))
GRUP_A = pd.DataFrame(GRUP_A)
GRUP_A[:] = "A"
A = pd.concat([A, GRUP_A], axis = 1)

#B ve B'nin Grubu
GRUP_B = np.arange(len(B))
GRUP_B = pd.DataFrame(GRUP_B)
GRUP_B[:] = "B"
B = pd.concat([B, GRUP_B], axis = 1)

#Tum veri
AB = pd.concat([A,B])
AB.columns = ["gelir","GRUP"]
print(AB.head())
print(AB.tail())




A = pd.DataFrame(
        [28, 33, 30, 29, 28, 29, 27, 31, 30, 32, 28, 33, 25, 29, 27, 31, 31, 30, 31, 34, 30, 32, 31, 34, 28, 32, 31, 28,
         33, 29])

B = pd.DataFrame(
        [31, 32, 30, 30, 33, 32, 34, 27, 36, 30, 31, 30, 38, 29, 30, 34, 34, 31, 35, 35, 33, 30, 28, 29, 26, 37, 31, 28,
         34, 33])

C = pd.DataFrame(
        [40, 33, 38, 41, 42, 43, 38, 35, 39, 39, 36, 34, 35, 40, 38, 36, 39, 36, 33, 35, 38, 35, 40, 40, 39, 38, 38, 43,
         40, 42])

AYRIK = pd.concat([A, B, C], axis=1)
AYRIK.columns = ["A", "B", "C"]
print("'AYRIK' Veri Seti: \n\n", AYRIK.head())

GRUPA = np.arange(len(A))
GRUPA = pd.DataFrame(GRUPA)
GRUPA[:] = "A"
A = pd.concat([A, GRUPA], axis=1)

GRUPB = np.arange(len(B))
GRUPB = pd.DataFrame(GRUPB)
GRUPB[:] = "B"
B = pd.concat([B, GRUPB], axis=1)

GRUPC = np.arange(len(C))
GRUPC = pd.DataFrame(GRUPC)
GRUPC[:] = "C"
C = pd.concat([C, GRUPC], axis=1)

BIRLIKTE = pd.concat([A, B, C])
BIRLIKTE

BIRLIKTE.columns = ["Vakit", "A-B-C"]
print("'BIRLIKTE' Veri Seti \n\n,", BIRLIKTE.head(), "\n")

import seaborn as sns

sns.boxplot(x="A-B-C", y="Vakit", data=BIRLIKTE);
plt.show()







#Dusuk Goller ve Pandas cevirimi

bjk1 = np.random.randint(0, 3, size = (18))

pd_bjk1 = pd.DataFrame(bjk1)

average_bjk1 = pd_bjk1.mean()

print ('average BJK 1', average_bjk1)



#Yuksek Goller ve Pandas cevirimi

bjk2 = np.random.randint(4, 8, size = (6))

pd_bjk2 = pd.DataFrame(bjk2)

average_bjk2 = pd_bjk2.mean()

print ('average BJK2', average_bjk2)



#Birlestirme

pd_bjk = pd.concat([pd_bjk1, pd_bjk2])

average_bjk = pd_bjk.mean()

print ('average BJK', average_bjk)



#Aykiri Degerleri Bulma

Q1 = pd_bjk.quantile(0.25)

Q3 = pd_bjk.quantile(0.75)

IQR = Q3 - Q1

alt_sinir = Q1 - 1.5*IQR

ust_sinir = Q3 + 1.5*IQR



#Aykiri Degerleri Ayiklama

t_pd_bjk = pd_bjk[~((pd_bjk < alt_sinir) | (pd_bjk > ust_sinir)).any(axis =1)]

t_pd_bjk.mean()

t_pd_bjk


planet = sns.load_dataset('tips')
df = pd.DataFrame(planet)
df= df.dropna()
#print(df.head())


df_total = pd.DataFrame(df["total_bill"])
print(sns.boxplot(x ="total_bill",data=df_total))
plt.show()

Q1 = df_total.quantile(0.25)
Q3 = df_total.quantile(0.75)
IQR = Q3-Q1
alt_sinir = Q1 - (1.5*IQR)
ust_sinir = Q3 + 1.5*IQR

print(alt_sinir)
print(ust_sinir)


diamonds = sns.load_dataset('titanic')
diamonds = diamonds.select_dtypes(include = ['float64', 'int64'])
df = diamonds.copy()
df = df.dropna()
df.head()
from sklearn.neighbors import LocalOutlierFactor
clf = LocalOutlierFactor(n_neighbors = 20, contamination = 0.1)

clf.fit_predict(df)
df_scores = clf.negative_outlier_factor_
np.sort(df_scores)[0:20]
esik_deger = np.sort(df_scores)[13]
#print(esik_deger)
#print(pd.DataFrame(np.sort(df_scores)).plot(stacked=True, xlim=[0,50], style='.-')) ## sıcrama noktası
plt.show()

V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])
df = pd.DataFrame(
        {"V1" : V1,
         "V2" : V2,
         "V3" : V3}
)
#print(df[df.isnull().all(axis = 1)])


a= df["V1"].fillna(df["V1"].mean())
#print(df.apply(lambda x: x.fillna(x.mean()), axis = 0))
"""


class Kareler():

    def __init__(self, maksimum):
        self.maksimum = maksimum

        self.sayı = 1

    def __iter__(self):
        return self

    def __next__(self):

        if (self.sayı <= self.maksimum):

            sonuc = self.sayı ** 2
            self.sayı += 1
            return sonuc
        else:
            self.sayı = 1
            raise StopIteration
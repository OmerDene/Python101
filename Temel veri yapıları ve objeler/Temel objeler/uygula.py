import pandas as pd
import numpy as np
# import seaborn as sns




#a = pd.Series([10,88,3,4,5])
#print(a.axes)
#print(a.tail(1))

#a = pd.Series([99,22,332,94,5], index = [0,1,2,3,4])
#a[2] = 1
#print(a[1:3])

#sozluk = {"reg":10, "log":11, "cart": 12}
#print(sozluk.keys())
#c= df = pd.Series(sozluk)
#print(df)
#a = pd.concat([c,c,c]) # iki ve daha fazla seriyi birlestirme
#print(a)

#seri = pd.Series([1,3,5,6,7 ],index= ["a","b","c","d","e"])
#print(seri)

#print(seri["b"])
#print(seri[["a","b"]])

#print(seri["a":"c"])

"""" Data Frame"""

#liste = [1,5,7,9,12]
#seri = pd.DataFrame(liste,columns=["merhaba"])
#print(seri)

#dizi = np.arange(9).reshape((3,3))
#print(dizi)
#df = pd.DataFrame(dizi,columns=["merhaba","yeni","dünya"],index=[3,5,7])
#print(df)
#liste = ["a","b","c"]

#df.columns = (liste) # degiskenlerin(kolonların isimlerinin güncellenmesi)
#print(df)
#c =df.rename(columns={"merhaba":"a","yeni":"b"}) # istedigimiz degiskenin ya da kolonun ismini güncelleme
#print(c)

#dizi = np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
#print(dizi)
#df = pd.DataFrame(dizi,columns=["omer","mehmet","masa"],index=[0,2,4])
#print(df)
#print(df.axes) # dataframe in genel bilgileri
#dizi = np.arange(9).reshape(3,3)
#print(dizi)
#df = pd.DataFrame(dizi,columns=["ilk kolon","ikinci kolon","ucuncu kolon"])
#a =df.drop(1,axis=0)
#print(a)
#print(df)
#df.drop(1, axis = 0, inplace = True) # bu sekilde inplace parametresi ile yazınca 1. satır komple gider ve yeni df degiskeni buna gore cagrılır
#print(df)
#liste = [0,1]
#a =df.drop(liste,axis=0)
#print(a)
#print(df)
#print(df[["ilk kolon","ikinci kolon"]])
#df["dördüncü kolon"] = df["ilk kolon"] * df["ikinci kolon"] # ekstra degisken ya da kolon bu sekilde eklenir.
#print(df)

#a =df.drop("dördüncü kolon",axis=1) # degisken ya da kolon silme(gecici)
#print(a)
#df.drop("dördüncü kolon", axis = 1, inplace = True) # bu sekilde kolon kalıcı gider(kalıcı)
#print(df)

#m = np.random.randint(1,30, size = (10,3))
#df = pd.DataFrame(m, columns = ["var1","var2","var3"])

#liste = ["var2","var1"]

#print(df["var2"][0:5])
#print(df[0:5][liste])


#print(df[df.var1>15][["var1","var2","var3"]])


#m = np.random.randint(1,30, size = (5,3))
#df1 = pd.DataFrame(m, columns = ["var1","var2","var3"])

#df2 = df1 + 99
#print(df2)
#df2.columns = ["var1","var2","deg3"]
#df3 = pd.concat([df1,df2],ignore_index=True)


#df3= pd.concat([df1, df2])

#df3= pd.concat([df1, df2], join = "inner")


#df3= pd.concat([df1,df2],axis=0)

#print(df3.reset_index(drop=True))

#df1 = pd.DataFrame({'calisanlar': ['Ali', 'Veli', 'Ayse', 'Fatma'],'grup': ['Muhasebe', 'Muhendislik', 'Muhendislik', 'İK']})
#print(df1)
#df2 = pd.DataFrame({'calisanlar': ['Ayse', 'Ali', 'Veli', 'Fatma'],'ilk_giris': [2010, 2009, 2014, 2019]})
#df3 = pd.merge(df1,df2 )
#print(df3)
#df3= pd.merge(df1, df2, on = "calisanlar") # calısanlar üzerinden grubu baglama
#df3= pd.merge(df1, df2)# ust satırla aynı cıktıyı verir
#print(df3)
#df5 = pd.DataFrame({'grup': ['Muhasebe', 'Muhasebe', 'Muhendislik', 'Muhendislik', 'İK', 'İK'], 'yetenekler': ['matematik', 'excel', 'kodlama', 'linux', 'excel', 'yonetim']})
#df6 =pd.merge(df3,df5)
#print(df6)
#df = sns.load_dataset("planets")
#print(df.describe().T)
#print(df.dropna().describe().T)

#df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],  'veri': [10,11,52,23,43,55]}, columns=['gruplar', 'veri'])
#print(df)
#df = sns.load_dataset("planets")
#print(df.describe())
#df.dropna().describe().T # dropna metodu eksik verilerin hesaplamalardan düsmesini saglıyor.

#df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],'veri': [10,11,52,23,43,55]}, columns=['gruplar', 'veri'])
#print(df)
#df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],'veri': [10,11,52,23,43,55]}, columns=['gruplar', 'veri'])

#a = df.groupby("gruplar").mean()
#print(a)

df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'degisken1': [10,23,33,22,11,99],
                   'degisken2': [100,253,333,262,111,969]},
                   columns = ['gruplar', 'degisken1', 'degisken2'])
#print(df)
df.iloc[5:6,2:3] = [3]
df.iloc[2:3,2:3] = [5]
#print(df)
#def filter_func(x): return x["degisken1"].std() > 9

#a = df.groupby("gruplar").filter(filter_fun,filter_func)



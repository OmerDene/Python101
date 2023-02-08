import pandas as pd
import numpy as np

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
dizi = np.arange(9).reshape(3,3)
#print(dizi)
df = pd.DataFrame(dizi,columns=["ilk kolon","ikinci kolon","ucuncu kolon"])
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

m = np.random.randint(1,30, size = (10,3))
df = pd.DataFrame(m, columns = ["var1","var2","var3"])

#liste = ["var2","var1"]

#print(df["var2"][0:5])
#print(df[0:5][liste])


#print(df[df.var1>15][["var1","var2","var3"]])



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

dizi = np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
#print(dizi)
df = pd.DataFrame(dizi,columns=["omer","mehmet","masa"],index=[0,2,4])
#print(df)
print(df.axes) # dataframe in genel bilgileri




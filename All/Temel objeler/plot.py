"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
"""
#planets = sns.load_dataset("planets")
#df = planets.copy()
#print(df["year"].value_counts().plot.barh())

#diamonds = sns.load_dataset('diamonds')
#df = diamonds.copy()
#l = ["Fair" , 'Good' , 'Very Good' , 'Premium'  ,"Ideal"]
#df["cut"] =pd.Categorical(df.cut,categories=l,ordered=True)
#print(df["cut"])
#print(df["cut"].value_counts().plot.barh().set_title("abcd"))

#print(sns.barplot(x = df.cut.value_counts().index, y = df.cut.value_counts(), data = df))

#print(sns.catplot(x = "cut", y = "price", data = df))
#print(sns.barplot(x = "cut", y = "price", hue = "color", data = df))
#print(sns.histplot(df["price"]))
#print(sns.histplot(df["price"], bins = 20))
#print(sns.kdeplot(df.price))
"""print((sns
 .FacetGrid(df,
              hue = "cut",
              height = 5,
              xlim = (0, 10000))
 .map(sns.kdeplot, "price", shade= True)
 .add_legend()
))
"""
#print(sns.catplot(x = "cut", y = "price", hue = "color", kind = "point", data = df))
#tips = sns.load_dataset("tips")
#df = tips.copy()
#print(sns.boxplot(y = "total_bill",x ="size", hue="sex", orient = "v",data=df))
#print(sns.barplot(x = "size", y = "total_bill", hue = "day", data = df))
#print(sns.catplot(x = "size", y = "total_bill", hue = "day", kind = "point", data = df))
#sns.scatterplot(x = "total_bill", y = "tip", data = df)
#sns.scatterplot(x = "total_bill", y = "tip", hue = "time",data = df)
#sns.scatterplot(x = "total_bill", y = "tip", hue = "time", style = "time", data = df)
#sns.scatterplot(x = "total_bill", y = "tip", hue = "day", style = "day", data = df)
#sns.scatterplot(x = "total_bill", y = "tip",  size = "smoker", data = df)
#sns.lmplot(x = "total_bill", y = "tip", data = df)
#sns.lmplot(x = "total_bill", y = "tip", hue = "time", col = "smoker", data = df)
#sns.lmplot(x = "total_bill", y = "tip", hue = "smoker", col = "time", row = "sex", data = df)
#iris = sns.load_dataset("iris")
#df = iris.copy()
#sns.scatterplot(x="sepal_length",y="sepal_width",data=df)
#sns.lmplot(x="sepal_length",y="sepal_width",data=df)
#sns.pairplot(df)
#sns.pairplot(df, hue = "species")
#sns.pairplot(df, kind = "reg", hue = "species")
#flights = sns.load_dataset('flights')
#df = flights.copy()
#print(df.isnull().values.any())
#df = df.pivot("month", "year", "passengers")
#print(sns.heatmap(df))
#sns.heatmap(df, annot = True, fmt = "d")
#sns.heatmap(df, annot = True, fmt = "d", linewidths =.1)
#fmri = sns.load_dataset("fmri")
#df = fmri.copy()
#sns.lineplot(x = "timepoint", y = "signal", data = df)
#sns.lineplot(x = "timepoint", y = "signal",  hue = "event", style = "event", markers = True,  dashes = False, data = df)
#sns.lineplot(x = "timepoint",  y = "signal",  hue = "region",style = "event", data = df)
#plt.show()
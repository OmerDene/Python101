import time


class Yazılımcı():
    def __init__(self,isim,soyisim,maaş,bildigi_diller  ):

        self.isim = isim
        self.soyisim = soyisim
        self.maaş = maaş
        self.bildigi_diller = bildigi_diller
    def bilgilerigöster(self):
        print(          "isim: {}\nsoyisim: {}\nmaaş: {}\nbildigi diller: {}\n ".format(self.isim,self.soyisim,self.maaş,self.bildigi_diller))
    def zam(self,zam_miktarı):


        self.maaş += zam_miktarı
    def dil_ekle(self,yeni_dil):
        self.bildigi_diller.append(yeni_dil)

yazılımcı = Yazılımcı("omer","dene",2000,["java ","python"])

yazılımcı.dil_ekle("C")
yazılımcı.zam(500)
yazılımcı.bilgilerigöster()




































import random
import time

class Kumanda():


    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi = ["Trt"],kanal = "Trt"):

        self.tv_durum = tv_durum

        self.tv_ses = tv_ses

        self.kanal_listesi = kanal_listesi

        self.kanal = kanal


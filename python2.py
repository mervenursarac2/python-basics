class Hayvan():
    def __init__(self, isim, yas):  # yapıcı/constructor metot
        self.isim = isim
        self.yas = yas

    def getYas(self):
        return self.yas

    def getAd(self):
        return self.isim


h1 = Hayvan("dog", 2)
h1_yas = h1.getYas()
print("h1 in yaşı :", h1_yas)

h1_isim = h1.getAd()
print("h1 in isim :", h1_isim)

h2 = Hayvan("cat", 3)
h2_yas = h2.getYas()
print("h2 in yaşı :", h2_yas)


class Makine():
    "hesap makinesi"

    def __init__(self, a, b):
        "başlangıç değerlerini ayarlar"
        # öznitelik alır
        """ pass """
        self.deger1 = a
        self.deger2 = b
        # pass
        # sonra oluşturursak pass

    def topla(self):
        " toplama a+b = sonuc -> return sonucs"
        sonuc = self.deger1+self.deger2
        return sonuc
    """pass"""

    def carp(self):
        "carpma a*b= sonuc -> return sonuc"
        sonuc = self.deger1*self.deger2
        return sonuc
    """pass"""

    def cikar(self):
        return self.deger1-self.deger2

    def bol(self):
        return self.deger1/self.deger2


x = 5
y = 2
h: Makine = Makine(x, y)
tSonuc = h.topla()
cSonuc = h.carp()
print("toplama sonuc: {}, çarpma sonucu: {}".format(tSonuc, cSonuc))

# ata sınıf --- parent


class Animal():
    def __init__(self):
        print("hayvan sınıfının yapıcı metotum")

    def sesCikar(self):
        print("hav,miyav,vak....")

    def hareket(self):
        print("zıplar,koşar,yürür..")
    # cocuk sınıf ----child


class kedi(Animal):
    def __init__(self):
        super().__init__()  # yazmasakta olur ata sınıfın init metodunu ezeriz metot overriding!!
        print("kedi sınıfı oluşturuldu")

    def sesCikar(self):
        print("miyav")

    def DokuzCan(self):  # diğer hayvanlardan ayrılan bir fonksiyon :D
        print("Bu sevimli hayvanlar hep dört ayak üstüne düşer")


k1 = kedi()
k1.sesCikar()  # ata sınıfı ezer
k1.hareket()
k1.DokuzCan()


class kus(Animal):
    def __init__(self):
        print("kus sınıfı oluşturldu")

    def ucma(self):
        print("kanatları vardır uçarlar")


kus1 = kus()
kus1.ucma()
kus1.hareket()

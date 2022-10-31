import time
import random

class bilgisayarlab():
    def __init__(self, lab_kapasitesi = 50, lab_durumu = "Açık", lab_ogrenci_sayisi = 0):
        self.lab_kapasitesi = lab_kapasitesi
        self.lab_durumu = lab_durumu
        self.lab_ogrenci_sayisi = lab_ogrenci_sayisi



    def lab_ac(self):
        if self.lab_durumu == "Açık":
            print("Lab zaten açık")
        else:
            print("Lab açılıyor")
            self.lab_durumu = "Açık"


    def lab_kapat(self):
        if self.lab_durumu == "Kapalı":
            print("Lab zaten kapalı")
        else:
            print("Lab kapatılıyor")
            self.lab_durumu = "Kapalı"


    def ogrenci_ekle(self, ogrenci_sayisi):
        if self.lab_durumu == "Kapalı":
            print("Lab kapalı, öğrenci eklenemiyor")
        elif self.lab_kapasitesi - self.lab_ogrenci_sayisi < ogrenci_sayisi:
            print("Labda yeterli boş alan yok")
        elif self.lab_kapasitesi - self.lab_ogrenci_sayisi >= ogrenci_sayisi:
            print("Öğrenci ekleniyor")
            time.sleep(1)
            self.lab_ogrenci_sayisi += ogrenci_sayisi
            print("Labdaki öğrenci sayısı: {}".format(self.lab_ogrenci_sayisi))
        elif self.lab_kapasitesi - self.lab_ogrenci_sayisi == 0:
            print("Lab dolu")
        else:
            print("Hatalı işlem")



    def ogrenci_cikar(self, ogrenci_sayisi):
        if self.lab_durumu == "Kapalı":
            print("Lab kapalı, öğrenci çıkarılamaz")
        elif self.lab_ogrenci_sayisi - ogrenci_sayisi < 0:
            print("Labda yeterli öğrenci yok")
        elif self.lab_ogrenci_sayisi - ogrenci_sayisi >= 0:
            print("Öğrenci çıkarılıyor")
            time.sleep(1)
            self.lab_ogrenci_sayisi -= ogrenci_sayisi
            print("Labdaki öğrenci sayısı: {}".format(self.lab_ogrenci_sayisi))
        elif self.lab_ogrenci_sayisi - ogrenci_sayisi == 0:
            print("Lab boş")
        else:
            print("Hatalı işlem")



    def lab_kapasite(self):
        print("Labdaki boş alan: {}".format(self.lab_kapasitesi - self.lab_ogrenci_sayisi))


    def lab_kapasite_arttir(self, kapasite):
        print("Lab kapasitesi arttırılıyor")
        time.sleep(1)
        self.lab_kapasitesi += kapasite
        print("Lab kapasitesi: {}".format(self.lab_kapasitesi))

    def lab_kapasite_azalt(self, kapasite):
        print("Lab kapasitesi azaltılıyor")
        time.sleep(1)
        self.lab_kapasitesi -= kapasite
        print("Lab kapasitesi: {}".format(self.lab_kapasitesi))




print("""

        1. Lab aç
        2. Lab kapat
        3. Öğrenci Ekle
        4. Öğrenci Çıkar
        5. Kapasiteyi Öğren
        6. Kapasiteyi Arttır
        7. Kapasiteyi Azalt

Çıkmak için q'ya bas.

""")

lab = bilgisayarlab()


while True:
    islem = input("İşlemi seçiniz: ")

    if islem == "q":
        print("Sonlandırılıyor")
        break
    elif islem == "1":
        lab.lab_ac()
    elif islem == "2":
        lab.lab_kapat()
    elif islem == "3":
        ogrenci_sayisi = int(input("Kaç öğrenci eklemek istiyorsunuz: "))
        lab.ogrenci_ekle(ogrenci_sayisi)
    elif islem == "4":
        ogrenci_sayisi = int(input("Kaç öğrenci çıkarmak istiyorsunuz: "))
        lab.ogrenci_cikar(ogrenci_sayisi)
    elif islem == "5":
        lab.lab_kapasite()
    elif islem == "6":
        kapasite = int(input("Kaç kişilik kapasite arttırmak istiyorsunuz: "))
        lab.lab_kapasite_arttir(kapasite)
    elif islem == "7":
        kapasite = int(input("Kaç kişilik kapasite azaltmak istiyorsunuz: "))
        lab.lab_kapasite_azalt(kapasite)
    else:
        print("Geçersiz işlem")

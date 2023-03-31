#Aldığı isim soy isim ile listeye öğrenci ekleyen

ogrenciListesi = ["Yağmur Gün","Ali Yılmaz","Beste Can"]
print(ogrenciListesi)

def addOgrenci():
    isim=input("Eklenecek öğrencinin ismini giriniz :")
    soyisim=input("Eklenecek öğrencinin soyismini giriniz:")
    sonuc=isim+ " " +soyisim
    ogrenciListesi.append(sonuc)
    print(ogrenciListesi)
addOgrenci()

print("************************************************")

#Aldığı isim soy isim ile eşleşen değeri listeden kaldıran

ogrenciListesi = ["Yağmur Gün","Ali Yılmaz","Beste Can"]
print(ogrenciListesi)

def addOgrenci():
    isim=input("Çıkarılacak öğrencinin ismini giriniz :")
    soyisim=input("Çıkarılacak öğrencinin soyismini giriniz:")
    sonuc=isim+ " " +soyisim
    ogrenciListesi.remove(sonuc)
    print(ogrenciListesi)
addOgrenci()

print("*************************************************")

#Listeye birden fazla öğrenci eklemeyi mümkün kılan

ogrenciListesi = ["Yağmur Gün","Ali Yılmaz","Beste Can"]
 
def addOgrenci():
    for ogrenci in range(5):
        isim=input("Eklenecek öğrencinin ismini giriniz :")
        soyisim=input("Eklenecek öğrencinin soyismini giriniz:")
        sonuc=isim+ " " +soyisim
        ogrenciListesi.append(sonuc)
addOgrenci()

def ogrencilerigoster():
    for isim in ogrenciListesi:
      print(isim)

ogrencilerigoster()

print("********************************************")

#Listedeki tüm öğrencileri tek tek ekrana yazdıran

def ogrencileriyazma():
    for ogrenciler in ogrenciListesi:
        print(ogrenciler)

ogrencileriyazma()

print("********************************************")
#Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan

def ogrenciNumarası():
    isim=input("Öğrencinin ismini giriniz :")
    soyisim=input("Öğrencinin soyismini giriniz:")
    sonuc=isim+ " " +soyisim
    print(ogrenciListesi.index(sonuc))
ogrenciNumarası()

print("********************************************")
#Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)

def ogrenciSil():
    i=0
    n = int(input("Kaç öğrenci çıkarılacak :"))
    while i<n:
        ogrenciNo = int(input("Çıkarılacak öğrenci no girin :"))
        ogrenciListesi.pop(ogrenciNo)
        i+=1
    print(ogrenciListesi)
ogrenciSil()
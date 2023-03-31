from human import Human


faiz = 1.59
vade = "36"
krediAdi= "ihtiyaç kredisi"

print(type(faiz)) #değişkenin tipinin ne olduğunu öğrenebiliriz.

print(int(vade)+12) #vade değişkenini stringten integer a çevirdik.

# cntl+ö hem açıklama satırı yapar hemde açıklama satırından çıkartır.

vade = 36 #int(input("lütfen istediğiniz vade sayısını giriniz:")) # dışardan veri isteme

print(type(vade))

vade = vade +12

#string interpolation
#seçtiğimiz vade sonucu ortaya çıkan vade:
print("seçtiğimiz vade sonucu ortaya çıkan vade:"+str(vade))
print("seçtiğiniz vade sonucu ortaya çıkan vade:{vadeSayisi}".format(vadeSayisi=vade))

isim = "halit"
metin = "Merhaba {name}".format(name=isim)
print(metin)

#f-string

metin = f"Hoşgeldiniz{isim}"
print(metin)

#listeler

krediler = ["ihtiyaç kredisi","taşıt kredisi","konut kredisi"]

print(type(krediler))
print(krediler)

# dizinin ilk elemanını çağırmak istersek 

print(krediler[0])

print(len(krediler)) # listede kaç eleman olduğunu öğrenebiliriz.

dizi = ["ihtiyaç kredisi",10,5.2]
print(dizi)

krediler.append("özel kredi") # listenin sonuna eklenir
print(krediler)

krediler.append("x kredisi")
print(krediler)

krediler.pop(0) # ilk index i silmiş olduk 
print(krediler)

krediler.remove("taşıt kredisi") # bulduğu ilk taşıt kredisi ismindekini silecek
print(krediler)

krediler.extend(["y kredisi","z kredisi"]) # diziye elemanları ekler 
print(krediler)

#for döngüsü i=0 i<10

for i in range(10): # range kısmı i nin içindeki değere ulaşana kadar 1 arttırtır.
    print("xx")
    print(i)
print("***************")
for i in range(5,10): # 5-10 arası 10 dahil değil
    print(i)
print("***************")
for i in range(0,50,10): # 0-50 arasını 10 ar 10 ar arttır.
    print(i)
print("**********")

krediler = ["ihtiyaç kredisi","taşıt kredisi","konut kredisi"]
for kredi in krediler:
    print(kredi)
print("*******")
for i in range(len(krediler)): #yukardaki kodla aynı işlemi yapar
    print(krediler[i])

print("****************")

# while True: # while içinde true olduğu sürece çalıştıran yapıdır. yani sonsuz döngüdür.
#     print("x")
# print("y") # y gözükmez x sonsuz döngüye girer ctrl + c ile durur.

i = 0
while i<10:
    print("x")
    i +=1
print("y")

print("****************")

while True:
    print("x")
    break # döngüyü kırdık ekranda sadece x gözükür.

print("****************")

i = 0
while i<len(krediler):
    if krediler[i]=="konut kredisi":
        break
    print(krediler[i])
    i+=1


#fonksiyonlar

fiyat = 100
indirim = 20 

def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayhello(name):
    print(f"merhaba {name}")

calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayhello("havva")

def calculateAndReturn(price,discount):
    return price-discount # çıktı olarak almaktan ziyade değer almak ve yeni bir isme atamak istiyoruz. o yüzden return kullandık.

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)

print("****************")


# instance => örnek
human1 = Human("Enes")
human1.talk("merhaba")
human1.walk()
print(human1)
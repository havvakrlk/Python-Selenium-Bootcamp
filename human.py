class Human:
    name = "Halit"
    #built - in
    #constructor
    #initialize
    def __init__(self,name): #yapıcı blok alanı 
        self.name = name
        print("Bir human instance'i üretildi")
    def __str__(self):
        return f"STR Fonksiyonundan dönen değer:{self.name}"
    def talk(self,sentence):
        print(f"{self.name} {sentence}") # self yazınca haliti alır ama sadece name yazarsak ercanı
    def walk(self):
        print("Human is walking..")

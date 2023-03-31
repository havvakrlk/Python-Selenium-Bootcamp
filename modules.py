#import matematik as m #takma isim verdik
from matematik import topla # sadece toplama işlemini import ettik
from human import Human
import random
from seleniumExample import webdriver

print(topla(10,20))
print(random.randint(0,100))

human1 = Human("Mirze")
human1.talk("merhaba")

chromDriver = webdriver.Chrome() 
#packages 
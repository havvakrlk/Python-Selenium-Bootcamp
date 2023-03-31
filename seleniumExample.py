from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window() #tam ekran yapma
driver.get("https://www.google.com.tr/?hl=tr")
sleep(5)
input = driver.find_element(By.NAME,"q")
input.send_keys("kodlamaio")
searchButton = driver.find_element(By.NAME,"btnK")
sleep(2)
searchButton.click()
sleep(2)
firstResult = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()
listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"kodlamaio sitesinde şu anda {len(listOfCourses)} adet kurs var")
while True:
    continue

 #chrome kapanmaması için koyduk   #sleep(10) # 10 sn chromu bekletir

 #html locators
 #full xpath
 # /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a

 #xpath
 # //*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a

# web scraping sitelerden veri kazıma
# data scraping
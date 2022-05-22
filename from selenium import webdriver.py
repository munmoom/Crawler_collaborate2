from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path= "./chromedriver.exe")

url = "https://shopping.naver.com/home/p/index.naver"
driver.get(url)

time.sleep(5)

serch=driver.find_element_by_xpath('//*[@id="_verticalGnbModule"]/div/div/div[2]/div/div[2]/form/fieldset/div/input')
serch.click()
driver.find_element_by_xpath('//*[@id="_verticalGnbModule"]/div/div/div[2]/div/div[2]/form/fieldset/div/input').send_keys('커피')
serch.send_keys(Keys.ENTER)

serch=driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[2]/div[3]/a')
serch.click()

serch=driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[2]/div[3]/ul/li[1]/a')
serch.click()

serch=driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[1]/a[4]')
serch.click()

driver.execute_script("window.scrollTo(0, 10000)")
driver.execute_script("window.scrollTo(10000, 0)")

prili=[]

while True:
 for j in range(1, 21):
   try:
     price_all = driver.find_element_by_xpath(f'//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[{j}]/li/div/div[2]/div[2]/strong/span/span').text
     prili.append(price_all)
   except:
     name = "NAN"
     pass
 if len(prili) == 20:
     break


print(prili)


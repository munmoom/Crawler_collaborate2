
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path= "./chromedriver.exe")

url = "https://shopping.naver.com/home/p/index.naver"
driver.get(url)

time.sleep(1)

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


li=[]
while True:
 for j in range(1, 21):
   n = len(li)
   try:
     name = driver.find_element_by_xpath(f'//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[{j}]/li/div/div[2]/div[1]/a').text
     li.append(name)
     if len(li) == n:
      name = driver.find_element_by_xpath(f'//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[{j}]/li/div[1]/div[2]/div[1]/a').text
      li.append(name)
   except:
     name = "NAN"
     pass
 if len(li) == 20:
     break

print(li)


import pandas as pd
ind = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sr = pd.Series(li, index =  ind)
sr

df=pd.DataFrame()
df['상품'] = li
df

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path= "./chromedriver.exe")

url = "https://www.ssg.com/main.ssg?ckwhere=ssg_gglekey&EKAMS=google.723.5136.21350.2033663.600584667&trackingDays=1&gclid=Cj0KCQjwm6KUBhC3ARIsACIwxBidNxkdJm0IWVl-IHfYKUV-83cJ3HEjhL4jatHFsD80HU_LTiAjlLEaAkb-EALw_wcB"
driver.get(url)


time.sleep(3)

serch=driver.find_element_by_xpath('//*[@id="ssg-query"]')
serch.click()
driver.find_element_by_xpath('//*[@id="ssg-query"]').send_keys('커피')
serch.send_keys(Keys.ENTER)


lister=driver.find_element_by_xpath('//*[@id="content"]/div[7]/div[1]/ul[2]/li[3]/div/a[2]')
lister.click()
 
serch=driver.find_element_by_xpath('//*[@id="content"]/div[7]/div[1]/ul[2]/li[2]/div/div/a/span[2]')
serch.click()

serch=driver.find_element_by_xpath('//*[@id="content"]/div[7]/div[1]/ul[2]/li[2]/div/div/div/ul/li[1]/a/span')
serch.click()


try:
  name = driver.find_element_by_xpath(f'//*[@id="item_unit_0000007024783"]/td[2]/div/div[2]/div/a').text
  print(f'---{name}---')
except:
  name = "NAN"
  pass
  print(f'---{name}---')

res = []




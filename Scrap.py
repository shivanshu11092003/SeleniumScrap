from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup




# options = webdriver.ChromeOptions()
# options.page_load_strategy = 'normal'
driver = webdriver.Chrome()


options = Options()
options.headless = True  # hide GUI
options.add_argument("--window-size=1920,1080")  # set window size to native GUI size
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://tech.kiet.edu/team-erp/")
driver.implicitly_wait(5)



try:


  a = driver.find_element(by=By.XPATH,value="(//section)[2]/div/div/div")
  actions = ActionChains(driver)
  actions.move_to_element(a).perform()
  time.sleep(3)

 

  batch = a.get_attribute("innerHTML")

  
  soup = BeautifulSoup(batch, 'html.parser')

  link =soup.find('div',class_='flex justify-start items-center')
  tag = link.find('a')
#   for finnal in soup.find_all('a', href=True):
  finalLink = tag['href']
  driver.get(finalLink)
  driver.implicitly_wait(5)

  b=driver.find_element(By.XPATH,"//*")
  time.sleep(3)

  print(b.text)
  #<section class="w-screen lg:px-28 my-10">

except TypeError as err:
    print("error",err)     







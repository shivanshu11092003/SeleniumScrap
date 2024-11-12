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
driver.implicitly_wait(9)


linkedinArray = []
try:



  for i in range(2,3):
    a = driver.find_elements(by=By.XPATH,value=f"(//section)[{i}]/div/div/div")
    for item in a:
      actions = ActionChains(driver)
      actions.move_to_element(item).perform()
      time.sleep(5)

 

      batch = item.get_attribute("innerHTML")

  
      soup = BeautifulSoup(batch, 'html.parser')

      link =soup.find('div',class_='flex justify-start items-center')
      tag = link.find('a')
      finalLink = tag['href']
 
      linkedinArray.append(finalLink)
  print(linkedinArray)

  for newItem in linkedinArray:
     newLink =  driver.get(f"{newItem}")


  # driver.implicitly_wait(15)


  # # send_keys("manuisgreat9@gmail.com")
  # time.sleep(3)

  # b=driver.find_element(By.XPATH,"//main/")
  # loginsoup = BeautifulSoup(  b.get_attribute("innerHTML"), 'html.parser')

  
  
  

  #<section class="w-screen lg:px-28 my-10">

except TypeError as err:
    print("error",err)     







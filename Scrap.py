from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import xlsxwriter



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


try:
  linkedinArray = []
  education =[]
  experience =[]




  for i in range(2,4):
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

  newLink =  driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")
  driver.implicitly_wait(5)
  username = driver.find_element(By.ID,"username")
  username.click()
  username.send_keys("sshivanshugupta11@gmail.com")
  password = driver.find_element(By.ID,"password")
  password.click()
  password.send_keys("Shivanshu@_123")
  btn = driver.find_element(By.TAG_NAME,"button")
  btn.click()
  time.sleep(4)
  for item in linkedinArray:
     driver.get(f"{item}")
     driver.implicitly_wait(5)




     section = driver.find_element(By.ID,"education")
     parentSectionEdu = section.find_element(By.XPATH,"..")
     education.append(parentSectionEdu.text)
 



     sectionExp = driver.find_element(By.ID,"experience")
     parentSectionExp = sectionExp.find_element(By.XPATH,"..")
     experience.append(parentSectionExp.text)
  workbook = xlsxwriter.Workbook('complete.xlsx')
  worksheet = workbook.add_worksheet()
  row = 0
  for i in linkedinArray:
     worksheet.write(row, 0, i)
     worksheet.write(row, 1, education[row])
     worksheet.write(row, 2, experience[row])
     row += 1
  
  workbook.close()
  

     






  # for newItem in linkedinArray:



  # # send_keys("manuisgreat9@gmail.com")
  # time.sleep(3)

  # b=driver.find_element(By.XPATH,"//main/")
  # loginsoup = BeautifulSoup(  b.get_attribute("innerHTML"), 'html.parser')

  
  
  

  #<section class="w-screen lg:px-28 my-10">

except TypeError as err:
    print("error",err)     







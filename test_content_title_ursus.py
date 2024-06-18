from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = "https://ursus-breweries.ro/"
driver = webdriver.Chrome()
response = driver.get(url)

## Accepting cookies 
ok_cookies = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonAcceptWrapper")
# print(ok_cookies)
ok_cookies.click()

## Search for the title tag on home page 
title = driver.find_element(By.XPATH, '/html/body/div[2]/div/section[1]/div/div[3]/h1').text
print(title)

if title == "Ursus Breweries":
    print('Success: The page title contains the expected text')
else:
    print('Error: The page title does not contain the expected text:', title)



input()
driver.close()




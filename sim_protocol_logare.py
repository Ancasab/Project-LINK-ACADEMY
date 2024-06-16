from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import time


driver = webdriver.Chrome()
response = driver.get(url="https://www.sheismomclub.com")

## Accepting cookies 
ok_cookies = driver.find_element(By.ID, "accept-cookie-policy")
print(ok_cookies)
ok_cookies.click()

# time.sleep = 3

## Go to Login 
login_link = driver.find_element(By.CSS_SELECTOR, 
".simc_nav.navbar-nav .nav-link")
login_link.click()

## Validare email and password

# time.sleep(3)

email_input = driver.find_element(By.NAME, "email")
email = email_input.send_keys("test_user2@ro")
time.sleep(3)
email_input.send_keys(Keys.ENTER)



password_input = driver.find_element(By.NAME, "password")
password = password_input.send_keys("12345678")
time.sleep(3)
password_input.send_keys(Keys.ENTER)

## Failing the login = recieved message: "Too many failed login requests received from your ip address (94.53.124.138), please wait for two hours." 
## <div class="alert alert-danger" role="alert">Too many failed login requests received from your ip address (94.53.124.138), please wait for two hours.</div>"

# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
# def este_valid(email):

#     return bool(re.fullmatch(regex, email))

# response = este_valid(email)



input("enter to close the program")

driver.close()
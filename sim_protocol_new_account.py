from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import time


driver = webdriver.Chrome()
response = driver.get(url="https://www.sheismomclub.com")

## Accepting cookies 
ok_cookies = driver.find_element(By.ID, "accept-cookie-policy")
# print(ok_cookies)
ok_cookies.click()

new_account = driver.find_element(By.LINK_TEXT, "Create account" )
new_account.click()

##Create accounts: test_user@ro, test_user1@ro, test_user2@ro

input_email = driver.find_element(By.NAME, "email")
new_user = input_email.send_keys("test_user2@ro")
time.sleep(3)
input_email.send_keys(Keys.ENTER)

password_input = driver.find_element(By.NAME, "password")
password = password_input.send_keys("12345678")
time.sleep(3)
password_input.send_keys(Keys.ENTER)

password_confirm = driver.find_element(By.NAME, "confirm_pass")
password_repeat = password_confirm.send_keys("12345678")
time.sleep(3)
password_confirm.send_keys(Keys.ENTER)

accept_terms = driver.find_element(By.ID, "terms_accepted")
accept_terms.click()

accept_gdpr = driver.find_element(By.ID, "gdpr_accepted")
accept_gdpr.click()

time.sleep(5)
create_account = driver.find_element(By.LINK_TEXT, "Create account")
time.sleep(5)
create_account.click()

time.sleep(20)

input()

driver.close()
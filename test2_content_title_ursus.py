from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import time




url = "https://ursus-breweries.ro/"
driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(options=chrome_options)

response = driver.get(url)

## cookies 
ok_cookies = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonAcceptWrapper")
ok_cookies.click()

## title on home page 
title = driver.find_element(By.XPATH, '/html/body/div[2]/div/section[1]/div/div[3]/h1').text
print(title)

def test_response():
    assert title == "Ursus Breweries"









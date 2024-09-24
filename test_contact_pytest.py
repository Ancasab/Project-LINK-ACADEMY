from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    driver = webdriver.Chrome()   
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(options=chrome_options)
    yield Driver 
    driver.quit()

# @pytest.fixture
# def browser():
#     chrome_options = Options()
#     chrome_options.add_argument("--disable-search-engine-choice-screen")
#     driver = webdriver.Chrome(options = chrome_options)
#     driver.maximize_window()
#     yield driver
#     driver.quit()

# Test accesare sectiunea 'PAGINA PRINCIPALA '  
def test_accesare_contact(browser:webdriver.Chrome):
    # accesare site
    browser.get("https://ursus-breweries.ro")
    time.sleep(10)
    
    # acceptare cookies
    COOKIE_ID = "CybotCookiebotDialogBodyLevelButtonAcceptWrapper"
    driver.find_element(By.ID, COOKIE_ID).click()

    # # Test acceptare cookie-uri pagina principala
    # cookie = browser.find_element(By.ID, "__gomagCookiePolicy")
    # cookie.click()
    # assert cookie, "Acest site nu utilizeaza Cookie-uri."
    # time.sleep(3)

    # # Test accesare sectiunea 'CONTACT'
    # contact = browser.find_element(By.XPATH, '//*[@id="main-menu"]/div/ul/li[8]/a')
    # contact.click()
    # assert contact, "Sectiunea 'CONTACT' nu este disponibila."
    # time.sleep(1)

    # # Test scroll pe verticala pagina sectiunii 'CONTACT'
    # time.sleep(2)
    # stopScrolling = 0
    # while True:
    #     stopScrolling += 1
    #     browser.execute_script("window.scrollBy(0,200)")
    #     if stopScrolling > 3:
    #         break
    #     time.sleep(1.1)
    # time.sleep(2)

    # browser.execute_script("window.scrollTo(0,450)")
    # time.sleep(3)
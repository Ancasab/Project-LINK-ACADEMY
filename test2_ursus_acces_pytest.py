import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(options=Options().add_argument("--disable-search-engine-choice-screen"))
    driver.get('https://ursus-breweries.ro')

    # Accept cookies
    wait = WebDriverWait(driver, 10)
    ok_cookies_button = wait.until(
        EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonAcceptWrapper"))
    )
    ok_cookies_button.click()

    yield driver
    driver.quit()

def test_access_marci(driver):
    driver.find_element(By.CSS_SELECTOR, ".button-menu.button-menu--js.aos-init.aos-animate").click()
    wait = WebDriverWait(driver, 10)
    marci_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Mărci"))
    )
    marci_link.click()

def test_access_over_18(driver):
    an = "1999"
    # driver.find_element(By.ID, "#year").send_keys(an)
    input_year = self.driver.find_element(By.CLASS_NAME, "year")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_to_be("https://ursus-breweries.ro/marci/"))
    
   

# def test_access_under_18(driver):
#     an = "2007"
#     driver.find_element(By.ID, "year").send_keys(an)
#     wait = WebDriverWait(driver, 10)
#     wait.until(EC.url_to_be("https://www.alcoolulnutefacemare.ro/"))

# def test_access_current_year(driver):
#     an = str(datetime.datetime.today().year - 18)
#     driver.find_element(By.ID, "year").send_keys(an)

#     wait = WebDriverWait(driver, 10)
#     error_message_element = wait.until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/form/h3[2]"))
#     )
#     assert error_message_element.text == "Vă rugăm să introduceți anul dvs de naștere"



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

import datetime
import random
import pytest
import time




# Accesare browser CHROME
@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(options = chrome_options)
    driver.maximize_window()
    return driver
    driver.quit()


# 14. Test accesare sectiunea 'CONTACT '  
def test_accesare_contact(browser:webdriver.Chrome):
    # accesare site
    browser().get("https://https://ursus-breweries.ro")
    time.sleep(2)

    # acceptare cookie-uri pagina principala
    cookie = browser.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonAcceptWrapper")
    cookie.click()
    # assert cookie, "Acest site nu utilizeaza Cookie-uri."
    time.sleep(3)

    # Test accesare sectiunea 'CONTACT'
    menu = browser.find_element(By.CSS_SELECTOR, ".button-menu.button-menu--js.aos-init.aos-animate")
    menu.click()
    contact = browser.find_element(By.LINK_TEXT, "Contact")
    contact.click()
    assert contact, "Sectiunea 'CONTACT' nu este disponibila."
    time.sleep(1)

    # Test scroll pe verticala pagina sectiunii 'CONTACT'
    time.sleep(2)
    stopScrolling = 0
    while True:
        stopScrolling += 1
        browser.execute_script("window.scrollBy(0,200)")
        if stopScrolling > 3:
            break
        time.sleep(1.1)
    time.sleep(2)

    browser.execute_script("window.scrollTo(0,450)")
    time.sleep(3)

    # Test completare formular 'Formular de contact'
    email = "stelian.dragne@yahoo.com"
    caseta_email = browser.find_element(By.NAME, "field-email")
    for letter in email:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_email.send_keys(letter)
    assert email, "Caseta 'Email' nu este vizibila."
    assert email, "Adresa de email introdusa nu este corecta."
    time.sleep(2)

    nume = "DRAGNE"
    caseta_nume = browser.find_element(By.NAME, "field-first_name")
    for letter in nume:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_nume.send_keys(letter)
    assert nume, "Caseta 'Nume' nu este vizibila."
    time.sleep(2)

    prenume = "Stelian"
    caseta_nume = browser.find_element(By.NAME, "field-first_name")
    for letter in nume:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_nume.send_keys(letter)
    assert prenume, "Caseta 'Prenume' nu este vizibila."
    time.sleep(2)


    mesaj = "Va rog sa ma contactati cat mai repede posibil. Comanda mea inca nu a fost livrata."
    caseta_mesaj = browser.find_element(By.NAME, "field-message")
    for letter in mesaj:
        time.sleep(random.uniform(0.05, 0.05))
        caseta_mesaj.send_keys(letter)
    assert mesaj, "Caseta 'Mesajul tau' nu este vizibila."
    time.sleep(2)

    browser.execute_script("window.scrollBy(0,150)")
    time.sleep(1)

    
    
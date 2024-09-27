import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def setup_teardown():

    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://ursus-breweries.ro")

    # Accept cookie 
    time.sleep(10)
    COOKIE_ID = "CybotCookiebotDialogBodyLevelButtonAcceptWrapper"
    driver.find_element(By.ID, COOKIE_ID).click()

    # # Improved approach using WebDriverWait
    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.invisibility_of_element_located((By.ID, "CybotCookiebotDialog")))

    # def access_marci:
    driver.find_element(By.CSS_SELECTOR, ".button-menu.button-menu--js.aos-init.aos-animate").click()
    
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Contact").click()
    time.sleep(10)

    yield driver
    # Teardown after test
    driver.quit()



def test_formular_contact_complete(setup_teardown):
    driver = setup_teardown
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div[2]/div[2]/span").click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,600 + window.scrollY);")
    driver.find_element(By.CSS_SELECTOR, "#wpcf7-f2652-o1 > form > h3")
    time.sleep(3)

    input_first_name = driver.find_element(By.NAME, "field-first_name")
    input_first_name.send_keys("Ionescu")
    input_first_name.send_keys(Keys.TAB)
    time.sleep(3)

    input_second_name = driver.find_element(By.NAME, "field-last_name")
    input_second_name.send_keys("Ion")
    input_second_name.send_keys(Keys.TAB)
    time.sleep(3)

    input_email = driver.find_element(By.NAME, "field-email")
    input_email.send_keys("ion_ionescu@yaho.com")
    input_email.send_keys(Keys.TAB)
    time.sleep(3)

    input_message = driver.find_element(By.NAME, "field-message")
    input_message.send_keys("testare contact")
    time.sleep(3)

    btn_trimite = driver.find_element(By.CLASS_NAME, "btn--submit-ro")
    btn_trimite.click()
    time.sleep(10)

    mesaj_confirmare = driver.find_element(By.CLASS_NAME, "wpcf7-response-output")
    time.sleep(10)
    assert mesaj_confirmare.text == 'Mesajul tău a fost trimis.'


def test_formular_contact_empty(setup_teardown):
    driver = setup_teardown
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div[2]/div[2]/span").click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,600 + window.scrollY);")
    driver.find_element(By.CSS_SELECTOR, "#wpcf7-f2652-o1 > form > h3")
    time.sleep(3)

    input_first_name = driver.find_element(By.NAME, "field-first_name")
    input_first_name.send_keys("")
    input_first_name.send_keys(Keys.TAB)
    time.sleep(3)

    input_second_name = driver.find_element(By.NAME, "field-last_name")
    input_second_name.send_keys("")
    input_second_name.send_keys(Keys.TAB)
    time.sleep(3)

    input_email = driver.find_element(By.NAME, "field-email")
    input_email.send_keys("")
    input_email.send_keys(Keys.TAB)
    time.sleep(3)

    input_message = driver.find_element(By.NAME, "field-message")
    input_message.send_keys("")
    time.sleep(3)

    btn_trimite = driver.find_element(By.CLASS_NAME, "btn--submit-ro")
    btn_trimite.click()
    time.sleep(10)

    lista_mesaje_eroare = driver.find_elements(By.CLASS_NAME, "wpcf7-not-valid-tip")
    for i in range(len(lista_mesaje_eroare)):
        assert lista_mesaje_eroare[i].text == 'Câmpul este obligatoriu.'
    
    mesaj_confirmare = driver.find_element(By.CLASS_NAME, "wpcf7-response-output")
    time.sleep(10)
    assert mesaj_confirmare.text == 'Unul sau mai multe câmpuri au o eroare. Te rog să verifici și să încerci din nou.'

def test_formular_email(setup_teardown):
    driver = setup_teardown
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div[2]/div[2]/span").click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,600 + window.scrollY);")
    driver.find_element(By.CSS_SELECTOR, "#wpcf7-f2652-o1 > form > h3")
    time.sleep(3)

    input_first_name = driver.find_element(By.NAME, "field-first_name")
    input_first_name.send_keys("jgkjhgkjh")
    input_first_name.send_keys(Keys.TAB)
    time.sleep(3)

    input_second_name = driver.find_element(By.NAME, "field-last_name")
    input_second_name.send_keys("dfhgjhvjh")
    input_second_name.send_keys(Keys.TAB)
    time.sleep(3)

    input_email = driver.find_element(By.NAME, "field-email")
    input_email.send_keys("aruifh")
    input_email.send_keys(Keys.ENTER)
    time.sleep(3)

    input_message = driver.find_element(By.NAME, "field-message")
    input_message.send_keys("email test")
    time.sleep(3)

    btn_trimite = driver.find_element(By.CLASS_NAME, "btn--submit-ro")
    btn_trimite.click()
    time.sleep(10)

    mesaj_eroare_email = driver.find_element(By.CLASS_NAME, "wpcf7-not-valid-tip")
    time.sleep(10)
    assert mesaj_eroare_email.text == 'Adresa de email introdusă este invalidă.'

    mesaj_confirmare = driver.find_element(By.CLASS_NAME, "wpcf7-response-output")
    time.sleep(10)
    assert mesaj_confirmare.text == 'Unul sau mai multe câmpuri au o eroare. Te rog să verifici și să încerci din nou.'

 

  



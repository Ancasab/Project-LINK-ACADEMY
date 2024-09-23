
from selenium.webdriver.common.action_chains import ActionChains

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class TestAcces(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get('https://ursus-breweries.ro')


        # Accept cookie consent dialog (adjust timeout as needed)
        time.sleep(10)
        COOKIE_ID = "CybotCookiebotDialogBodyLevelButtonAcceptWrapper"
        self.driver.find_element(By.ID, COOKIE_ID).click()

         # Improved approach using WebDriverWait
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.ID, "CybotCookiebotDialog")))
    
        # def access_contact(self):
        self.driver.find_element(By.CSS_SELECTOR, ".button-menu.button-menu--js.aos-init.aos-animate").click()
       
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Contact").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div[2]/div[2]/span").click()
        time.sleep(3)

        self.driver.execute_script("window.scrollTo(0,500 + window.scrollY);")

        time.sleep(5)
    
    def tearDown(self):
        self.driver.close()


    def insereaza_nume_familie(self, nume_familie):
        input_first_name = self.driver.find_element(By.NAME, "field-first_name")
        input_first_name.send_keys(nume_familie).send_keys(Keys.ENTER)

    def insereaza_prenume(self, prenume):
        input_second_name = self.driver.find_element(By.NAME, "field-last_name")
        input_second_name.send_keys(prenume).send_keys(Keys.ENTER)

    def insereaza_email(self, email):
        input_email = self.driver.find_element(By.NAME, "field-email")
        input_email.send_keys(email).send_keys(Keys.ENTER)

    def insereaza_mesaj(self, mesaj):
        input_message = self.driver.find_element(By.NAME, "field-message")
        input_message.send_keys(mesaj).send_keys(Keys.ENTER)

    def buton_trimitere_formular(self):
        submit_button = self.driver.find_element(By.CSS_SELECTOR, ".wpcf7-f2652-o1 > form > div:nth-child(7) > button")


#   ________________________________________________  
#     def test_nume_familie_alfanumeric(self):
#         self.insereaza_nume_familie("Popescu")
    
    def test_nume_familie_empty(self):
        self.insereaza_nume_familie("jgtfvlii;jo")
        # assert self.driver.find_elements(By.XPATH, "/html/body/div[1]/section[3]/div/div[1]/form/div[2]/span/span[2]") == "Câmpul este obligatoriu"
        assert self.driver.find_elements(By.CSS_SELECTOR, ".wpcf7-form-control-wrap.field-first_name span")[0] == "Câmpul este obligatoriu"

#         __________________

   

# class TestAcces(unittest.TestCase):

#     def setUp(self):
#         # Create a WebDriver instance
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()

#     def tearDown(self):
#         # Close the browser
#         self.driver.quit()

#     def test_nume_familie_empty(self):
#         # Access the web page
#         self.driver.get("https://ursus-breweries.ro")

#         # Wait for the input field to be present and visible
#         wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
#         input_first_name = wait.until(EC.presence_of_element_located((By.NAME, "field-first_name")))  # Replace with the correct locator

#         # Enter an empty string and press Enter
#         input_first_name.send_keys("")
#         input_first_name.send_keys(Keys.ENTER)

        

    # def test_submit_valid_form(self, nume_familie, prenume, email, mesaj):

    #     # Completăm formularul cu date valide
    #     # nume_familie = "Popescu"
    #     for letter in nume_familie:
    #         time.sleep(random.uniform(0.05, 0.05))
    #         self.insereaza_nume_familie.send_keys(letter)
    #         time.sleep(3)

    #     # prenume = "Marin"
    #     for letter in prenume:
    #         time.sleep(random.uniform(0.05, 0.05))
    #         self.insereaza_prenume.send_keys(letter)
    #         time.sleep(3)

    #     # email = "popescu-m@yaho.com"   
    #     for letter in email:
    #         time.sleep(random.uniform(0.05, 0.05))
    #         self.insereaza_email.send_keys(letter)
    #         time.sleep(3)

    #     # mesaj = "Aceasta este un mesaj de test pentru formularul de contact."  
    #     for letter in email:
    #         time.sleep(random.uniform(0.05, 0.05))   
    #         self.insereaza_mesaj.send_keys(mesaj)
    #         time.sleep(3)

    #     # Trimitem formularul
    #     self.buton_trimitere_formular.click()

    #     self.test_submit_valid_form (nume_familie = "Popescu", prenume = "Marin", email = "popescu-m@yaho.com" , mesaj = "Aceasta este un mesaj de test pentru formularul de contact.")

    #     # Așteptăm pentru mesajul de confirmare sau redirecționare (ajustează selectorul/URL-ul după cum este necesar)
    #     try:
    #         WebDriverWait(self.driver, 10).until(
    #             EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".wpcf7-f2652-o1 > form > div.wpcf7-response-output"), "Mesajul tău a fost trimis.")
    #         )
    #         print("Mesajul de confirmare a fost găsit.")
    #     except TimeoutException:
    #         # Verifică dacă a avut loc o redirecționare sau dacă există alt element de confirmare
    #         print("Nu s-a găsit mesajul de confirmare. Verificați dacă a avut loc o redirecționare sau dacă selectorul este corect.")


     

    
    


    



if __name__ == "__main__":
    unittest.main()
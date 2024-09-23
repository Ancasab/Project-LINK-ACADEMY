
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import unittest
from selenium.webdriver.chrome.options import Options

class TestContactForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://ursus-breweries.ro")

        # Improved approach using explicit wait
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.ID, "CybotCookiebotDialog")))

        # Access contact page
        self.access_contact_page()

    def tearDown(self):
        self.driver.quit()

    def access_contact_page(self):
        menu_button = self.driver.find_element(By.CSS_SELECTOR, ".button-menu.button-menu--js.aos-init.aos-animate")
        ActionChains(self.driver).move_to_element(menu_button).perform()
        time.sleep(10)  # Short wait for menu hover (adjust as needed)

        contact_link = self.driver.find_element(By.LINK_TEXT, "Contact")
        contact_link.click()

        # Scroll down to contact form (if necessary)
        time.sleep(2)  # Wait for page to load (adjust as needed)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def insereaza_nume_familie(self, nume_familie):
        input_first_name = self.driver.find_element(By.NAME, "field-first_name")
        input_first_name.send_keys(nume_familie + Keys.ENTER)  # Use Keys.ENTER to submit

    def insereaza_prenume(self, prenume):
        input_second_name = self.driver.find_element(By.NAME, "field-last_name")
        input_second_name.send_keys(prenume + Keys.ENTER)

    def insereaza_email(self, email):
        input_email = self.driver.find_element(By.NAME, "field-email")
        input_email.send_keys(email + Keys.ENTER)

    def insereaza_mesaj(self, mesaj):
        input_message = self.driver.find_element(By.NAME, "field-message")
        input_message.send_keys(mesaj)

    def buton_trimitere_formular(self):
        submit_button = self.driver.find_element(By.CSS_SELECTOR, ".wpcf7-f2652-o1 > form > div:nth-child(7) > button")
        return submit_button

    def test_submit_valid_form(self):
        # Arrange
        nume_familie = "Popescu"
        prenume = "Marin"
        email = "popescu-m@yaho.com"
        mesaj = "Aceasta este un mesaj de test pentru formularul de contact."

        # Act
        self.access_contact_page()
        self.insereaza_nume_familie(nume_familie)
        self.insereaza_prenume(prenume)
        self.insereaza_email(email)
        self.insereaza_mesaj(mesaj)
        submit_button = self.buton_trimitere_formular()
        submit_button.click()

        # assert driver.find_elements('By.CSS_SELECTOR, ".wpcf7-f2652-o1 > form > div.wpcf7-response-output"')[0].text == "Mesajul tău a fost trimis."

        # Assert (adjust selector as needed)
        # try:
        #     WebDriverWait(self.driver, 10).until(
        #         EC.text_to_be_present_in_element(
        #             (By.CSS_SELECTOR, ".wpcf7-f2652-o1 > form > div.wpcf7-response-output"), "Mesajul tău a fost trimis."
        #         )
        #     )
        #     self.assertTrue(True, "Mesajul de confirmare a fost găsit.")  # Assert că testul a trecut
        # except TimeoutException:
        #     self.fail("Nu s-a găsit mesajul de confirmare. Verificați dacă a avut loc o redirecționare sau dacă selectorul este corect.")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, ".wpcf7-f2652-o1 > form > div.wpcf7-response-output"), "Mesajul tău a fost trimis."
                )
            )
            print("Test trecut: Mesajul de confirmare a fost găsit.")  # Adăugat print
            self.assertTrue(True, "Mesajul de confirmare a fost găsit.")
        except TimeoutException:
            print("Test eșuat: Nu s-a găsit mesajul de confirmare.")  # Adăugat print
            self.fail("Nu s-a găsit mesajul de confirmare. Verificați dacă a avut loc o redirecționare sau dacă selectorul este corect.")
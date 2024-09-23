# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import datetime
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options




# class TestAcces(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         chrome_options = Options()
#         chrome_options.add_argument("--disable-search-engine-choice-screen")
#         self.driver = webdriver.Chrome(options=chrome_options)

#         self.driver.get('https://ursus-breweries.ro')


#         # Accept cookie consent dialog (adjust timeout as needed)
#         time.sleep(10)
#         COOKIE_ID = "CybotCookiebotDialogBodyLevelButtonAcceptWrapper"
#         self.driver.find_element(By.ID, COOKIE_ID).click()

#          # Improved approach using WebDriverWait
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.invisibility_of_element_located((By.ID, "CybotCookiebotDialog")))

#         # def access_marci(self):
#         self.driver.find_element(By.CSS_SELECTOR, ".button-menu.button-menu--js.aos-init.aos-animate").click()
       
#         time.sleep(3)
#         self.driver.find_element(By.LINK_TEXT, "Contact").click()
#         time.sleep(3)

#         self.driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div[2]/div[2]/span").click()
#         time.sleep(5)

#         self.driver.execute_script("window.scrollTo(0,500 + window.scrollY);")

#         time.sleep(5)

#     def tearDown(self):
#         self.driver.close()


#     def insereaza_nume_familie(self, nume_familie):
#         # input_first_name = self.driver.find_element(By.NAME, "field-first_name")
#         wait = WebDriverWait(self.driver, 10)
#         input_first_name = wait.until(EC.presence_of_element_located((By.NAME, "field-first_name")))
#         input_first_name.click()
#         input_first_name.send_keys(nume_familie)
#         input_first_name.send_keys(Keys.ENTER)

    # def insereaza_prenume(self, prenume):
    #     input_second_name = self.driver.find_element(By.NAME, "field-last_name")
    #     input_second_name.send_keys(prenume).send_keys(Keys.ENTER)

    # def insereaza_email(self, email):
    #     input_email = self.driver.find_element(By.NAME, "field-email")
    #     input_email.send_keys(email).send_keys(Keys.ENTER)

    # def insereaza_mesaj(self, mesaj):
    #     input_message = self.driver.find_element(By.NAME, "field-message")
    #     input_message.send_keys(mesaj).send_keys(Keys.ENTER)


    # def test_nume_familie_empty(self):

    #     self.insereaza_nume_familie("")
    #     assert self.driver.find_elements(By.XPATH, "//*[@id="wpcf7-f2652-o1"]/form/div[7]/text()") == "Unul sau mai multe câmpuri au o eroare. Te rog să verifici și să încerci din nou."
        
        # self.insereaza_nume_familie("")
        # assert self.driver.find_elements(By.XPATH, "/html/body/div[1]/section[3]/div/div[1]/form/div[2]/span/span[2]") == "Câmpul este obligatoriu"
        
        # self.insereaza_nume_familie("")
        # assert self.driver.find_elements(By.XPATH, "//*[@id="wpcf7-f2652-o1"]/form/div[7]/text()]") == "Unul sau mai multe câmpuri au o eroare. Te rog să verifici și să încerci din nou."

    # def test_nume_familie(self):
    #     self.insereaza_nume_familie("Dragomir")
    #     assert self.driver.find_elements(By.XPATH, "/html/body/div[1]/section[3]/div/div[1]/form/div[2]/span/span[2]") == "Câmpul este obligatoriu"

# //*[@id="wpcf7-f2652-o1"]/form/div[7]/text()

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time



class TestAcces(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # Disable search engine choice screen
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get('https://ursus-breweries.ro')

        # Accept cookie consent dialog (adjust timeout as needed)
        wait = WebDriverWait(self.driver, 10)
        try:
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonAcceptWrapper")))
            cookie_button.click()
        except TimeoutException:
            print("Cookie consent dialog not found.")  # Handle potential absence of dialog

        # Wait for cookie dialog disappearance (alternative approach)
        wait.until(EC.invisibility_of_element_located((By.ID, "CybotCookiebotDialog")))

    def test_contact_form_with_empty_last_name(self):
        # Navigate to 'Contact' section
        self.driver.find_element(By.CSS_SELECTOR, ".button-menu.button-menu--js.aos-init.aos-animate").click()
        time.sleep(2)  # Consider using explicit wait instead of fixed sleep
        self.driver.find_element(By.LINK_TEXT, "Contact").click()
        time.sleep(2)

        # Scroll down (alternative: use explicit wait for specific element)
        self.driver.execute_script("window.scrollTo(0, 500 + window.scrollY);")
        time.sleep(2)  # Consider using explicit wait instead of fixed sleep

        # **Call the insereaza_nume_familie method here**
        self.insereaza_nume_familie("")

        # Assert expected error message (handle potential timeouts)
        wait = WebDriverWait(self.driver, 10)
        # error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='wpcf7-f2652-o1']/form/div[7]/text()")))
        error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "wpcf7-f2652-o1 > form > div:nth-child(3) > span > span")))
        
        time.sleep(5)

        self.assertEqual(error_message.text, "Câmpul este obligatoriu")

        # error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "wpcf7-f2652-o1 > form > div.wpcf7-response-output")))
        
        # time.sleep(10)

        # self.assertEqual(error_message.text, "Unul sau mai multe câmpuri au o eroare. Te rog să verifici și să încerci din nou.")

      
        


    def insereaza_nume_familie(self, nume_familie):
        wait = WebDriverWait(self.driver, 10)
        input_last_name = wait.until(EC.presence_of_element_located((By.NAME, "field-last_name")))
        input_last_name.click()
        input_last_name.send_keys(nume_familie)
        input_last_name.send_keys(Keys.ENTER)

    def tearDown(self):
        self.driver.quit()

    # def insereaza_nume_familie(self, nume_familie):
    #     wait = WebDriverWait(self.driver, 10)
    #     input_last_name = wait.until(EC.presence_of_element_located((By.NAME, "field-last_name")))
    #     input_last_name.click()
    #     input_last_name.send_keys(nume_familie)
    #     input_last_name.send_keys(Keys.ENTER)

 

    # def tearDown(self):
    #     self.driver.quit()






if __name__ == "__main__":
    unittest.main()

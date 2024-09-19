import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import time
import datetime



class TestAcces(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ursus-breweries.ro')

        time.sleep(2)
        COOKIE_ID = "CybotCookiebotDialogBodyLevelButtonAcceptWrapper"
        self.driver.find_element(By.ID, COOKIE_ID).click()

        self.driver.find_element(By.CSS_SELECTOR, ".button-menu.button-menu--js.aos-init.aos-animate").click()
       
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Contact").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div[2]/div[2]/span").click()
        time.sleep(5)

        self.driver.execute_script("window.scrollTo(0,500 + window.scrollY);")

        time.sleep(5)
        

       

    def tearDown(self):
        self.driver.close()


    def insereaza_nume_familie(self, nume_familie):
        input_first_name = self.driver.find_element(By.NAME, "field-first_name")
        input_first_name.send_keys(nume_familie).send_keys("ENTER")

    def insereaza_prenume(self, prenume):
        input_second_name = self.driver.find_element(By.NAME, "field-last_name")
        input_second_name.send_keys(prenume).send_keys("ENTER")

    def insereaza_email(self, email):
        input_email = self.driver.find_element(By.NAME, "field-email")
        input_email.send_keys(email).send_keys("ENTER")

    def insereaza_mesaj(self, mesaj):
        input_message = self.driver.find_element(By.NAME, "field-message")
        input_message.send_keys(mesaj).send_keys("ENTER")


    def test_nume_familie_empty(self):
        self.insereaza_nume_familie("")
        assert self.driver.find_elements(By.XPATH, "/html/body/div[1]/section[3]/div/div[1]/form/div[2]/span/span[2]") == "Câmpul este obligatoriu"




     

    
    


    



if __name__ == "__main__":
    unittest.main()
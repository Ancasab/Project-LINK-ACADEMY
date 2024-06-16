import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime



class TestAcces(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ursus-breweries.ro')

        time.sleep(2)
        COOKIE_ID = "CybotCookiebotDialogBodyLevelButtonAcceptWrapper"
        self.driver.find_element(By.ID, COOKIE_ID).click()

    # def access_marci(self):
        self.driver.find_element(By.CSS_SELECTOR, ".button-menu.button-menu--js.aos-init.aos-animate").click()
       
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Mărci").click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()



    def insereaza_an(self, an_nastere):
        input_year = self.driver.find_element(By.CLASS_NAME, "year")
        input_year.send_keys(an_nastere)

    def insereaza_luna(self, luna):
        input_month =  self.driver.find_element(By.NAME, "month")
        input_month.send_keys(luna)


    def insereaza_zi(self, zi):
        input_day = self.driver.find_element(By.NAME, "day")
        input_day.send_keys(zi)

    def test_access(self):
        an = "1999"
        self.insereaza_an(an)
        assert self.driver.current_url == "https://ursus-breweries.ro/marci/"

    def test_fara_access(self):
        an = "2007"
        self.insereaza_an(an)
        time.sleep(10)
        assert self.driver.current_url == "https://www.alcoolulnutefacemare.ro/"


    def test_access_an_current(self):
        an = "2006" ## an curent - 18 ani
        an = str(datetime.datetime.today().year - 18)
        print("an curent:", an)
        self.insereaza_an(an)
        
        time.sleep(10)
        mesaj = "Vă rugăm să introduceți anul dvs de naștere"
        print("text:", self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/form/h3[2]").text)

        assert self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/form/h3[2]").text == mesaj
    

    def test_access_luna_currenta(self):
        an = "2006" ## an curent - 18 ani
        an = str(datetime.datetime.today().year - 18)
        print("an curent:", an)
        self.insereaza_an(an)
        
        time.sleep(10)
        mesaj = "Vă rugăm să introduceți anul dvs de naștere"
        print("text:", self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/form/h3[2]").text)

        assert self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/form/h3[2]").text == mesaj

        luna = str(datetime.datetime.today().month)
        luna = luna.zfill(2)
        self.insereaza_luna(luna)

        mesaj = "Vă rugăm să introduceți anul dvs de naștere"
        print("text:", self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/form/h3[2]").text)


        zi = str(datetime.datetime.today().day)
        zi = zi.zfill(2)

        self.insereaza_zi(zi)
        assert self.driver.current_url == "https://ursus-breweries.ro/marci/"

        time.sleep(20)


if __name__ == "__main__":
    unittest.main()
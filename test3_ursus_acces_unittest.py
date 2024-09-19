import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime


class TestAcces(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get('https://ursus-breweries.ro')

        # Accept cookies using Explicit Wait
        wait = WebDriverWait(self.driver, 10)
        ok_cookies_button = wait.until(
            EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonAcceptWrapper"))
        )
        ok_cookies_button.click()

    def access_marci(self):
        self.driver.find_element(By.CSS_SELECTOR, ".button-menu.button-menu--js.aos-init.aos-animate").click()
        wait = WebDriverWait(self.driver, 10)
        marci_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Mărci"))
        )
        marci_link.click()

    def tearDown(self):
        self.driver.close()

    def insereaza_an(self, an_nastere):
        input_year = self.driver.find_element(By.ID, "year")
        input_year.send_keys(an_nastere)

    # def insereaza_luna(self, luna):
    #     input_month = self.driver.find_element(By.ID, "month")
    #     input_month.send_keys(luna)

    # def insereaza_zi(self, zi):
    #     input_day = self.driver.find_element(By.ID, "day")
    #     input_day.send_keys(zi)

    # def test_access(self):
    #     an = "1999"
    #     self.insereaza_an(an)
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.url_to_be("https://ursus-breweries.ro/marci/"))

    # def test_fara_access(self):
    #     an = "2007"
    #     self.insereaza_an(an)
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.url_to_be("https://www.alcoolulnutefacemare.ro/"))

    # def test_access_an_current(self):
    #     an = str(datetime.datetime.today().year - 18)
    #     print("an curent:", an)
    #     self.insereaza_an(an)

    #     wait = WebDriverWait(self.driver, 10)
    #     error_message_element = wait.until(
    #         EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/form/h3[2]"))
    #     )
    #     expected_message = "Vă rugăm să introduceți anul dvs de naștere"
    #     assert error_message_element.text == expected_message

    # def test_access_luna_currenta(self):
    #     an = str(datetime.datetime.today().year - 18)
    #     print("an curent:", an)
    #     self.insereaza_an(an)

    #     wait = WebDriverWait(self.driver, 10)
    #     error_message_element = wait.until(
    #         EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/form/h3[2]"))
    #     )
    #     expected_message = "Vă rugăm să introduceți anul dvs de naștere"
    #     assert error_message_element.text == expected_message

    #     luna = str(datetime.datetime.today().month)
    #     luna = luna.zfill(2)
    #     self.insereaza_luna(luna)

    #     wait = WebDriverWait(self.driver, 10)
    #     error_message

    if __name__ == "__main__":
        unittest.main()
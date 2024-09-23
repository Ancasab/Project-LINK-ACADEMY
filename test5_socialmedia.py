# %%
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
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

    def tearDown(self):
        self.driver.close()

    def access_media (self, media_id):
        try:
            social_media = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, media_id))
            )
        except TimeoutException:
            # Handle the case where the element is not found within the timeout period
            self.fail(f"Media element with ID '{media_id}' not found on the page.")
            return  # Exit the function if element is not found

        social_media.click()

    def test_linkedin():
        time.sleep(3)
        driver.maximize_window()
        linkedin = self.access_media(menu-item-179)
        time.sleep(3)
        assert driver.current_url == "https://www.linkedin.com/company/ursus-breweries/" 
        # or driver.current_url == "https://www.linkedin.com/uas/login?session_redirect=%2Fcompany%2F2979195%2F"

        
      


    # def test_facebook():
    #     time.sleep(3)
    #     driver.maximize_window()
    #     facebook = driver.find_element(By.ID, "menu-item-176")
    #     facebook.click()
    #     assert driver.current_url == "https://www.facebook.com/UrsusBreweriesRomania/"

    


# driver = webdriver.Chrome()
# chrome_options = Options()
# chrome_options.add_argument("--disable-search-engine-choice-screen")
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://ursus-breweries.ro")

# time.sleep(10)
# COOKIE_ID = "CybotCookiebotDialogBodyLevelButtonAcceptWrapper"
# driver.find_element(By.ID, COOKIE_ID).click()

# def test_linkedin():
#     time.sleep(3)
#     driver.maximize_window()
#     linkedin = driver.find_element(By.ID, "menu-item-179")
#     linkedin.click()
#     time.sleep(3)
#     # linkedin_message = driver.find_element(By.CSS_SELECTOR, ".join-now") 
#     # assert linkedin_message == " Join now "
#     assert driver.current_url == "https://www.linkedin.com/company/ursus-breweries/"


# def test_facebook():
#     time.sleep(3)
#     driver.maximize_window()
#     facebook = driver.find_element(By.ID, "menu-item-176")
#     facebook.click()
#     assert driver.current_url == "https://www.facebook.com/UrsusBreweriesRomania/"



# driver.quit()

# javascript_code = """
#     var consent_fb = document.getElementsById(":r3:")
#     consent_fb.click
# """

# # driver.execute_script(javascript_code)

# time.sleep(3)
# facebook_messages = driver.find_elements(By.XPATH, "//*[@id=":r3:"]")
# facebook_messages 

# driver.maximize_window()
# facebook_messages = driver.find_elements(By.CSS_SELECTOR, "#\:r3\:")
# facebook_messages 


if __name__ == "__main__":
    unittest.main()

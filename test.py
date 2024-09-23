import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options 



class TestAcces(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://ursus-breweries.ro")

        # Improved approach using explicit wait for cookie consent
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonAcceptWrapper"))
        ).click()
        # Ensure cookie consent is accepted before proceeding

    def tearDown(self):
        self.driver.quit()

    def access_media(self, media_id):
        """
        Accesses a specific media element using its ID and waits for its presence.

        Args:
            media_id (str): The ID of the media element to access.

        Returns:
            WebElement or None: The located element or None if not found within the timeout.

        Raises:
            AssertionError: If the current URL doesn't match the expected URL after clicking.
        """

        try:
            social_media = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, media_id))
            )
            social_media.click()
            return social_media  # Return the element for further actions (if needed)
        except TimeoutException:
            self.fail(f"Media element with ID '{media_id}' not found on the page.")
            return None  # Indicate element not found

    def test_linkedin(self):
        """
        Tests accessing the LinkedIn media element and verifies redirection.
        """

        # Use `self.access_media` for improved error handling and potential future actions
        linkedin_element = self.access_media("menu-item-179")  # Replace with correct ID
        if linkedin_element is not None:  # Check if element was found
            # Wait for page load (adjust as needed)
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be("https://www.linkedin.com/company/ursus-breweries/")
            )
            self.assertEqual(
                self.driver.current_url, "https://www.linkedin.com/company/ursus-breweries/"
            )
        else:
            # Handle the case where the "menu-item-179" element is not found
            self.fail("LinkedIn element with ID 'menu-item-179' not found.")

# Execute the tests
if __name__ == "__main__":
    unittest.main()
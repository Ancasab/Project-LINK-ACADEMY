from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(options=chrome_options)

@pytest.fixture(scope="function")
def setup_teardown():
    # Setup WebDriver
    driver = webdriver.Chrome()  
    driver.get("https://ursus-breweries.ro")  # LinkedIn login page URL
    yield driver
    # Teardown after test
    driver.quit()

#Test deschidere linkedIn
def test_deschidere_linkedin(setup_teardown):
    driver = setup_teardown
    time.sleep(3)
    driver.maximize_window()
    linkedin = driver.find_elements(By.ID, "menu-item-179")
    linkedin[0].click()

    all_tabs = driver.window_handles
    driver.switch_to.window(all_tabs[1])
    time.sleep(3)

    linkedin_message = driver.find_element(By.CSS_SELECTOR, "button.artdeco-global-alert-action")
    time.sleep(5)
    linkedin_message.text
    assert linkedin_message.text == "Accept"
    time.sleep(5)



def test_accesare_facebook(setup_teardown):
    driver = setup_teardown
    time.sleep(3)
    driver.maximize_window()
    facebook = driver.find_elements(By.ID, "menu-item-176")
    facebook[0].click()

    all_tabs = driver.window_handles
    driver.switch_to.window(all_tabs[1])
    time.sleep(3)

    facebook_message = driver.find_element(By.CSS_SELECTOR, "body > div.__fb-light-mode.x1n2onr6.x1vjfegm > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x1exxf4d.x13fuv20.x178xt8z.x1l90r2v.x1pi30zi.x1swvt13 > div > div:nth-child(2) > div.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.x9f619.x3nfvp2.xdt5ytf.xl56j7k.x1n2onr6.xh8yej3 > div > div.x6s0dn4.x78zum5.xl56j7k.x1608yet.xljgi0e.x1e0frkt")
    time.sleep(5)
    assert facebook_message.text == "Allow all cookies"
    time.sleep(5)

    




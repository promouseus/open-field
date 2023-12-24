from selenium import webdriver
from selenium.webdriver.common.by import By
import time

firefox_options = webdriver.FirefoxOptions()
#firefox_options.headless = True
firefox_options.set_preference('layout.css.devPixelsPerPx','1.0') #this sets high resolution

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444',
    options=firefox_options
)
driver.set_window_size(1920, 3240) # Headless / fullscreen

driver.get("https://www.bol.com")

time.sleep(3)

#cookie_button = driver.find_element_by_css_selector('button[data-test="consent-modal-confirm-btn"]')
try:
   cookie_button = driver.find_element(By.CSS_SELECTOR, 'button[id="cookie_accept"]')
   cookie_button.click()
except:
   print("No cookie pop-up")




#element = driver.find_element(By.TAG_NAME, 'body')
#element_png = element.screenshot_as_png
#with open("image_full.png", "wb") as file:
#    file.write(element_png)

#firefox_elem = driver.find_element_by_tag_name('html')
#firefox_elem.screenshot('./image_full2.png')

time.sleep(3)

driver.save_screenshot('./image.png')

time.sleep(3)

driver.quit()

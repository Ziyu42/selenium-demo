from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.flash_message = (By.ID, "flash")
        self.logout_button = (By.LINK_TEXT, "Logout")

    
    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_flash_message(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.flash_message)).text
    
    def get_flash_attribute(self):
        flash = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.flash_message))
        return flash.get_attribute("class")
    
    def get_flash_background(self):
        flash = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.flash_message))
        return flash.value_of_css_property("background")

    def logout(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.logout_button)).click()

    def get_current_url(self):
        return self.driver.current_url
    
    def is_logout_button_displayed(self):
        try:
            logout_btn = WebDriverWait(self.driver, 5).until((EC.visibility_of_element_located(self.logout_button)))
            return logout_btn.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False
    
    def secure_area(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h2")))

    def perform_failed_login_attempts(self, username, password, attempts=3):
        for _ in range(attempts):
            self.login(username, password)
            time.sleep(5)
    
    def refresh_page(self):
        self.driver.refresh()

    def is_on_login_page(self):
        return "login" in self.get_current_url()
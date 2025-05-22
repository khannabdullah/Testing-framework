import time
from selenium.webdriver.support.ui import WebDriverWait # type: ignore

from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from basepage.Basepage import Basepage_base
from utils.ValidationEngine import ValidationEngine

class LoginPage(Basepage_base):

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)
        # ve = ValidationEngine()

        # user_name = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        # user_name.click()
        # user_name.send_keys(username)
        # time.sleep(2)
        # pass_word = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
        # pass_word.click()
        # pass_word.send_keys(password)
        # ve.is_valid_username("Password", password)
        # time.sleep(2)
        # login_button = wait.until(EC.presence_of_element_located((By.ID, 'kt_login_signin_submit')))
        # login_button.click()
        # time.sleep(2)
        ve = ValidationEngine()

    # Validate input data before sending it to the UI
        ve.is_valid_username("Username", username)
        ve.is_valid_password("Password", password)

        # If there are any validation errors, print and stop execution
        if ve.errors:
            for error in ve.errors:
                print("Validation Error:", error)
            return  # or raise Exception, or log result, etc.

        # Proceed with interacting with the UI only if inputs are valid
        username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        password_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
        login_button = wait.until(EC.presence_of_element_located((By.ID, 'kt_login_signin_submit')))

        username_field.clear()
        username_field.send_keys(username)

        password_field.clear()
        password_field.send_keys(password)

        login_button.click()

    
    def open(self, url):
        self.driver.get(url)
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SystemTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test_signup_success(self):
        # Open the registration page
        self.driver.get("http://localhost/Money-Daily1/Money-Daily/LoginRegister.php")

        # Click the sign-up button to go to the registration form
        sign_up_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "sign-up-btn"))
        )
        sign_up_btn.click()

        # Wait until the registration form is fully loaded
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sign-up-form")))

        # Locate input fields for registration
        name_input = self.driver.find_element(By.NAME, "name")
        mother_name_input = self.driver.find_element(By.NAME, "mother_name")
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")

        # Fill out the registration form
        name_input.send_keys("Sita Sudarsono")
        mother_name_input.send_keys("Erni")
        email_input.send_keys("sita@gmail.com")
        password_input.send_keys("sita123")

        # Submit the registration form
        submit_button = self.driver.find_element(By.XPATH, "//input[@value='Sign up']")
        self.driver.execute_script("arguments[0].click();", submit_button)

        # Wait for alert (increase the timeout if necessary)
        WebDriverWait(self.driver, 30).until(EC.alert_is_present())

        # Accept the alert
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()

        

        # Perform login after successful registration
        self.login("sita@gmail.com", "sita123")


    def login(self, username, password):
        # Open the login page
        self.driver.get("http://localhost/Money-Daily1/Money-Daily/LoginRegister.php")  # replace with the actual path to your HTML file

        # Wait until the login form is fully loaded
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))

        # Locate input fields for login
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")

        # Fill out the login form
        email_input.send_keys(username)
        password_input.send_keys(password)

        # Submit the login form
        submit_button = self.driver.find_element(By.XPATH, "//input[@value='Login']")
        self.driver.execute_script("arguments[0].click();", submit_button)

        # Wait until the alert appears
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        # Accept the alert
        alert = self.driver.switch_to.alert
        print(alert.text)  # Print the alert text to see the message
        alert.accept()

if __name__ == "__main__":
    unittest.main()

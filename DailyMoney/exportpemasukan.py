import time  # Import time module for delays
import unittest  # Import unittest module for testing
from selenium import webdriver  # Import webdriver from Selenium for browser automation
from selenium.webdriver.common.by import By  # Import By from Selenium for element selection
from selenium.webdriver.support.ui import Select  # Import Select for handling dropdowns
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for waiting
from selenium.webdriver.support import expected_conditions as EC  # Import expected_conditions for explicit wait conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class SystemTest(unittest.TestCase):
    def setUp(self):
        # Initialize WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Add a delay before closing WebDriver
        time.sleep(5)
        # Close WebDriver
        self.driver.quit()

    def login(self, username, password):
        # Open login page
        self.driver.get("http://localhost/Money-Daily/LoginRegister.php")

        # Find username and password input elements by name attribute
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")

        # Enter username and password
        email_input.send_keys(username)
        password_input.send_keys(password)

        # Click Login button
        login_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        login_button.click()

        # Wait for page to load
        time.sleep(5)

    def test_export_income_report(self):
        # Perform login
        self.login("sita@gmail.com", "sita12345")
        
        # Open financial report page
        self.driver.get("http://localhost/Money-Daily/laporan.php")
        time.sleep(2)

        # Find and click the export button for income report
        export_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='export-pemasukan.php']"))
        )
        export_button.click()
        

        # Wait to ensure the export action is completed
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()

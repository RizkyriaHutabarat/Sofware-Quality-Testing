import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SystemTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def login(self, username, password):
        self.driver.get("http://localhost/Money-Daily/LoginRegister.php")

        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")

        email_input.send_keys(username)
        password_input.send_keys(password)

        login_button = self.driver.find_element(By.CSS_SELECTOR, ".sign-in-form input[type='submit']")
        login_button.click()

        time.sleep(2)

    def logout(self):
        # Asumsikan URL halaman dashboard atau halaman utama setelah login
        self.driver.get("http://localhost/Money-Daily/index.php")
        time.sleep(2)

        # Klik tombol dropdown user
        user_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "userDropdown"))
        )
        user_dropdown.click()

        # Klik tombol logout di dalam dropdown
        logout_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-target='#logoutModal']"))
        )
        logout_link.click()

        time.sleep(2)

        # Tunggu hingga modal logout muncul dan klik tombol "Keluar" di dalam modal
        confirm_logout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='logoutModal']//a[@class='btn btn-primary' and text()='Keluar']"))
        )
        confirm_logout_button.click()
        time.sleep(2)



    def test_system_flow(self):
        self.login("yaya@gmail.com", "yaya12345")
        # Here you can perform other test steps like input, edit, delete, etc.

        # Call logout method
        self.logout()

if __name__ == "__main__":
    unittest.main()

import time  # Impor modul time untuk penundaan
import unittest  # Impor modul unittest untuk pengujian
from selenium import webdriver  # Impor modul webdriver dari Selenium untuk otomatisasi browser
from selenium.webdriver.common.by import By  # Impor modul By dari Selenium untuk memilih elemen
from selenium.webdriver.support.ui import Select  # Impor modul Select untuk menangani dropdown
from selenium.webdriver.support.ui import WebDriverWait  # Impor WebDriverWait untuk menunggu
from selenium.webdriver.support import expected_conditions as EC  # Impor expected_conditions untuk kondisi eksplisit
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class SystemTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test_register_then_login(self):
        # Open the registration page
        self.driver.get("http://localhost/Money-Daily1/Money-Daily/LoginRegister.php")

        # Click the sign-up button to go to the registration form
        sign_up_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "sign-up-btn"))
        )
        sign_up_btn.click()

        # Wait for the registration form to load
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "sign-up-form")))
        time.sleep(2)

        # Fill out the registration form
        name_input = self.driver.find_element(By.NAME, "name")
        mother_name_input = self.driver.find_element(By.NAME, "mother_name")
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")

        name_input.send_keys("yaya")
        mother_name_input.send_keys("yuyu")
        email_input.send_keys("yaya@gmail.com")
        password_input.send_keys("yaya12345")

        # Submit the registration form automatically
        registration_form = self.driver.find_element(By.CLASS_NAME, "sign-up-form")
        registration_form.submit()

        time.sleep(2)

        # Call login method after successful registration
        self.login_after_registration("yaya@gmail.com", "yaya12345")

    def login_after_registration(self, username, password):
        # Membuka halaman login
        self.driver.get("http://localhost/Money-Daily/LoginRegister.php")

        # Mencari elemen input username dan password menggunakan nama atribut
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")

        # Memasukkan nama pengguna dan kata sandi
        email_input.send_keys(username)
        password_input.send_keys(password)

        # Klik tombol Login
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".sign-in-form input[type='submit']")
        login_button.click()

        # Tunggu hingga halaman berpindah
        time.sleep(5)
    

if __name__ == "__main__":
    unittest.main()

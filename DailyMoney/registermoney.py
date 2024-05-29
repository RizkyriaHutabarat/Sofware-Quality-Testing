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
        # Membuka halaman web
        self.driver.get("http://localhost/Money-Daily/register.php")

        # Tunggu hingga halaman sepenuhnya dimuat
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sign-up-form")))

        # Temukan elemen-elemen input untuk registrasi
        name_input = self.driver.find_element(By.NAME, "name")
        mother_name_input = self.driver.find_element(By.NAME, "mother_name")
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")

        # Mengisi formulir registrasi
        name_input.send_keys("Sita Sudarsono")
        mother_name_input.send_keys("Erni")
        email_input.send_keys("sita@gmail.com")
        password_input.send_keys("sita12345")

        # Klik tombol submit untuk registrasi
        submit_button = self.driver.find_element(By.CSS_SELECTOR, ".sign-up-form input[type='submit']")
        submit_button.click()

        # Tunggu hingga notifikasi muncul
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "swal2-confirm")))

        # Menutup notifikasi setelah registrasi berhasil
        swal = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
        swal.click()

        # Setelah berhasil mendaftar, langsung login
        self.login("sita@gmail.com", "sita12345")

    def login(self, username, password):
        # Membuka halaman login
        self.driver.get("http://localhost/Money-Daily/LoginRegister.php")

        # Mencari elemen input username dan password menggunakan nama atribut
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")

        # Memasukkan nama pengguna dan kata sandi
        email_input.send_keys(username)
        password_input.send_keys(password)

        # Klik tombol Login
        login_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        login_button.click()

        # Tunggu hingga halaman berpindah
        time.sleep(5)


    def test_system_flow(self):

        self.login("sita@gmail.com", "sita12345")


if __name__ == "__main__":
    unittest.main()

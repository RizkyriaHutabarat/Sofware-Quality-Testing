import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Tambahkan penundaan waktu sebelum menutup WebDriver
        time.sleep(5)

        # Menutup WebDriver
        self.driver.quit()

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

    def test_valid_login(self):
        # Jalankan pengujian login dengan kredensial valid
        self.login("kia@gmail.com", "1234567")

        # Verifikasi bahwa pengguna berhasil login dan menuju ke halaman yang diinginkan
        current_url = self.driver.current_url
        self.assertEqual(current_url, "http://localhost/Money-Daily/index.php")

    

if __name__ == "__main__":
    unittest.main()

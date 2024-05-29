import time  # Impor modul time untuk penundaan
import unittest  # Impor modul unittest untuk pengujian
from selenium import webdriver  # Impor modul webdriver dari Selenium untuk otomatisasi browser
from selenium.webdriver.common.by import By  # Impor modul By dari Selenium untuk memilih elemen
from selenium.webdriver.common.keys import Keys  # Impor modul Keys dari Selenium untuk mengirim kunci
from selenium.webdriver.support.ui import Select  # Impor modul Select untuk menangani dropdown

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

    def inputpemasukan(self):
        # Membuka halaman cek kebugaran
        self.driver.get("http://localhost/Money-Daily/pendapatan_banyak.php")

        time.sleep(2)

        # Mencari elemen input menggunakan nama atribut
        tgl_pemasukan_input = self.driver.find_element(By.NAME, "tgl_pemasukan3")
        jumlah_input = self.driver.find_element(By.NAME, "jumlah3")
        sumber_input = Select(self.driver.find_element(By.NAME, "sumber3"))
        deskripsi_input = self.driver.find_element(By.NAME, "deskripsi3")

        # Memasukkan nilai ke dalam input
        tgl_pemasukan_input.send_keys("05/15/2024")
        jumlah_input.send_keys("2000000")
        sumber_input.select_by_visible_text("Freelancer")
        deskripsi_input.send_keys("Pemasukan dari freelancing")

        # Tunggu hingga tombol submit muncul
        time.sleep(2)

        # Klik tombol Submit
        button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button.click()

    def test_system_flow(self):
        # Jalankan pengujian login
        self.login("sita@gmail.com", "sita12345")

        # Jalankan pengujian cek kebugaran
        self.inputpemasukan()

if __name__ == "__main__":
    unittest.main()

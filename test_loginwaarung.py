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
        self.driver.get("http://localhost/Project-3-master/Project-3-master/admin/login.php")

        # Mencari elemen input username dan password menggunakan nama atribut
        email_input = self.driver.find_element(By.NAME, "user")
        password_input = self.driver.find_element(By.NAME, "pass")

        # Memasukkan nama pengguna dan kata sandi
        email_input.send_keys(username)
        password_input.send_keys(password)

        # Klik tombol Login
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[name='login']")
        login_button.click()

        time.sleep(2)

    def cek_produk(self):
        # Membuka halaman cek kesehatan
        self.driver.get("http://localhost/Project-3-master/Project-3-master/admin/index.php?halaman=produk")

        time.sleep(2)

        # Lakukan pengujian cek kesehatan
        # Lakukan implementasi pengujian cek kesehatan di sini

    

    def test_system_flow(self):
        # Jalankan pengujian login
        self.login("admin", "123456")

        self.cek_produk()
        # Tambahkan penundaan setelah login
        time.sleep(2)

        # Lakukan pengujian pada halaman selanjutnya setelah login
        # Misalnya, Anda bisa menambahkan pengujian untuk memastikan login berhasil dan menuju ke halaman yang diinginkan


if __name__ == "__main__":
    unittest.main()

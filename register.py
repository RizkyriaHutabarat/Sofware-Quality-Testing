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
        self.driver.get("https://healhero.my.id/signup.html")

        # Tunggu hingga halaman sepenuhnya dimuat
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "af-submit-app-category")))

        # Temukan elemen dropdown untuk memilih peran
        role_dropdown = self.driver.find_element(By.ID, "af-submit-app-category")
        role_dropdown.click()
        role_dropdown.send_keys(Keys.ARROW_DOWN)

        time.sleep(2)

        # Temukan tombol submit dan klik
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']") 
        button.click()

        # Tunggu hingga halaman registrasi sepenuhnya dimuat
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

        # Temukan elemen-elemen input untuk registrasi
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        namalengkap_input = self.driver.find_element(By.ID, "namalengkap")
        tanggallahir_input = self.driver.find_element(By.ID, "tanggallahir")
        jeniskelamin_input = self.driver.find_element(By.ID, "jeniskelamin")
        nomorhp_input = self.driver.find_element(By.ID, "nomorhp")
        alamat_input = self.driver.find_element(By.ID, "alamat")

        # Mengisi formulir registrasi
        email_input.send_keys("siti@gmail.com")
        password_input.send_keys("siti12345")
        namalengkap_input.send_keys("siti Sudarsono")
        tanggallahir_input.send_keys("28/06/2003")  # Format tanggal sesuai dengan input yang diterima
        jeniskelamin_input.send_keys(Keys.ARROW_DOWN)  # Memilih gender
        nomorhp_input.send_keys("628122028273")
        alamat_input.send_keys("Jl. Padjajaran No. 24")

        # Tunggu sebentar agar formulir terisi dengan benar
        time.sleep(2)

        # Klik tombol submit untuk registrasi menggunakan JavaScript
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        self.driver.execute_script("arguments[0].click();", submit_button)

        # Tunggu hingga notifikasi muncul
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "swal2-confirm")))

        # Menutup notifikasi setelah registrasi berhasil
        swal = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
        swal.click()

        # Setelah berhasil mendaftar, langsung login
        self.login("siti@gmail.com", "siti12345")

    def login(self, username, password):
        # Membuka halaman login
        self.driver.get("https://healhero.my.id/signin.html")

        # Mencari elemen input username dan password menggunakan XPath
        email_input = self.driver.find_element(By.XPATH, "//input[@id='email']")
        password_input = self.driver.find_element(By.XPATH, "//input[@id='password']")

        # Memasukkan nama pengguna dan kata sandi
        email_input.send_keys(username)
        password_input.send_keys(password)

        time.sleep(2)

        # Klik tombol Login
        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        time.sleep(2)

        # Cari dan klik tombol OK pada popup
        swal = self.driver.find_element(By.CLASS_NAME, "swal2-confirm")
        swal.click()

    def home(self):
        # Membuka halaman cek kesehatan
        self.driver.get("https://healhero.my.id/pengguna/index.html")

        time.sleep(2)
    
    # def test_system_flow(self):
    #     # Jalankan pengujian login
    #     self.test_signup_success()

    #     self.login("tejo@gmail.com", "tejo12345")

    #      # Jalankan pengujian halaman utama
    #     self.home()

if __name__ == "__main__": 
    unittest.main()
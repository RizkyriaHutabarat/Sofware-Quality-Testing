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
        # Membuka halaman input pemasukan
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

    def editpemasukan(self):
        # Membuka halaman daftar pemasukan
        self.driver.get("http://localhost/Money-Daily/pendapatan.php")
        time.sleep(2)

        # Klik tombol edit pada data pemasukan yang ingin diedit
        edit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'fa-edit')]"))
        )
        edit_button.click()

        # Tunggu hingga modal edit terbuka
        time.sleep(2)

        # Mencari elemen input pada modal edit
        tgl_pemasukan_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "tgl_pemasukan"))
        )
        jumlah_input = self.driver.find_element(By.NAME, "jumlah")
        sumber_input = Select(self.driver.find_element(By.NAME, "id_sumber"))
        deskripsi_input = self.driver.find_element(By.NAME, "deskripsi")

        # Menghapus nilai lama dan memasukkan nilai baru ke dalam input
        tgl_pemasukan_input.clear()
        tgl_pemasukan_input.send_keys("05/16/2024")
        jumlah_input.clear()
        jumlah_input.send_keys("500000")

        # Pilih opsi dari dropdown berdasarkan nilai
        sumber_input.select_by_value("2")  # Ubah nilai sesuai dengan nilai opsi "Freelancer" dalam dropdown

        deskripsi_input.clear()
        deskripsi_input.send_keys("Pemasukan dari proyek baru")

        # Tunggu hingga tombol Ubah muncul
        time.sleep(2)

        # Klik tombol Ubah pada modal edit
        ubah_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Ubah')]")
        ubah_button.click()

        # Tunggu untuk memastikan bahwa tombol Ubah telah diklik dan pembaruan telah selesai
        time.sleep(2)

    def export_income_report(self):
        # Membuka halaman laporan
        self.driver.get("http://localhost/Money-Daily/laporan.php")
        time.sleep(2)

        # Mencari dan mengklik tombol ekspor laporan pemasukan
        export_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='export-pemasukan.php']"))
        )
        export_button.click()

        # Tunggu untuk memastikan bahwa aksi ekspor selesai
        time.sleep(5)


    def test_system_flow(self):
        # Jalankan pengujian login
        self.login("sita@gmail.com", "sita12345")
        # Jalankan pengujian input pemasukan
        self.inputpemasukan()
        # Jalankan pengujian edit pemasukan
        self.editpemasukan()
        # Jalankan pengujian ekspor laporan setelah edit pemasukan
        self.export_income_report()

if __name__ == "__main__":
    unittest.main()

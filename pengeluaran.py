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
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".sign-in-form input[type='submit']")
        login_button.click()

        # Tunggu hingga halaman berpindah
        time.sleep(5)

    def inputpengeluaran(self):
        # Membuka halaman input pemasukan
        self.driver.get("http://localhost/Money-Daily/pengeluaran_banyak.php")
        time.sleep(2)

        tgl_pengeluaran_input = self.driver.find_element(By.NAME, "tgl_pengeluaran3")
        jumlah_input = self.driver.find_element(By.NAME, "jumlah3")
        sumber_input = Select(self.driver.find_element(By.NAME, "sumber3"))
        deskripsi_input = self.driver.find_element(By.NAME, "deskripsi3")

        # Fill out the form with appropriate data
        tgl_pengeluaran_input.send_keys("05/16/2024")  # Format date according to input type
        jumlah_input.send_keys("200000")  # Input amount
        sumber_input.select_by_visible_text("Fashion")  # Select an option from dropdown
        deskripsi_input.send_keys("Pengeluaran untuk pakaian")

         # Tunggu hingga tombol submit muncul
        time.sleep(2)

        # Klik tombol Submit
        button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button.click()

    def editpengeluaran(self):
        # Membuka halaman daftar pemasukan
        self.driver.get("http://localhost/Money-Daily/pengeluaran.php")
        time.sleep(2)

        # Klik tombol edit pada data pemasukan yang ingin diedit
        edit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'fa-edit')]"))
        )
        edit_button.click()

        # Tunggu hingga modal edit terbuka
        time.sleep(2)

        # Mencari elemen input pada modal edit
        tgl_pengeluaran_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "tgl_pengeluaran"))
        )
        jumlah_input = self.driver.find_element(By.NAME, "jumlah")
        keperluan_input = Select(self.driver.find_element(By.NAME, "id_sumber"))
        deskripsi_input = self.driver.find_element(By.NAME, "deskripsi")

        # Clear old values and enter new values
        tgl_pengeluaran_input.clear()
        tgl_pengeluaran_input.send_keys("05/16/2024")  # Example date
        jumlah_input.clear()
        jumlah_input.send_keys("25000")  # Example amount

        # Select an option from dropdown
        keperluan_input.select_by_value("8")  # Example option

        deskripsi_input.clear()
        deskripsi_input.send_keys("Pengeluaran untuk transportasi harian")  # Example description

        # Wait for the update button to appear
        time.sleep(2)

        # Click on the update button in the modal
        update_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Ubah')]")
        update_button.click()

        # Tunggu untuk memastikan bahwa tombol Ubah telah diklik dan pembaruan telah selesai
        time.sleep(2)    

    def deletepengeluaran(self):
        # Membuka halaman daftar pengeluaran
        self.driver.get("http://localhost/Money-Daily/pengeluaran.php")
        time.sleep(2)

        # Klik tombol ubah untuk membuka modal
        edit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-target='#myModal43']"))
        )
        edit_button.click()

        # Tunggu hingga modal terbuka dan tombol hapus dapat diklik
        delete_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-danger' and contains(text(), 'Hapus')]"))
        )
        delete_button.click()

        # Tunggu hingga dialog konfirmasi muncul
        confirm_delete = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        confirm_delete.accept()

        # Tunggu untuk memastikan bahwa data telah dihapus dan kembali ke halaman daftar pengeluaran
        time.sleep(2)

 
    


    def test_valid(self):
        # Jalankan pengujian login dengan kredensial valid
        self.login("yaya@gmail.com", "yaya12345")
        self.inputpengeluaran()
        self.editpengeluaran()
        self.deletepengeluaran()
        


if __name__ == "__main__":
    unittest.main()

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

    def login(self, username, password):
        self.driver.get("http://localhost/Money-Daily/LoginRegister.php")

        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")

        email_input.send_keys(username)
        password_input.send_keys(password)

        login_button = self.driver.find_element(By.CSS_SELECTOR, ".sign-in-form input[type='submit']")
        login_button.click()

        time.sleep(5)

    def input_pengeluaran(self):
        self.driver.get("http://localhost/Money-Daily/pengeluaran.php")
        time.sleep(2)

        tambah_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-success[data-target='#myModalTambah']"))
        )
        tambah_button.click()

        # Tunggu hingga modal terbuka
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "myModalTambah"))
        )
        time.sleep(2)

        # Mencari elemen input pada modal menggunakan XPath
        tgl_pengeluaran_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='tgl_pengeluaran']"))
        )
        jumlah_input1 = self.driver.find_element(By.XPATH, "//input[@name='jumlah']")
        sumber_input1 = Select(self.driver.find_element(By.XPATH, "//select[@name='sumber']"))
        deskripsi_input1 = self.driver.find_element(By.XPATH, "//input[@name='deskripsi']")

        # Clear old values and enter new values
        tgl_pengeluaran_input.clear()
        tgl_pengeluaran_input.send_keys("05/16/2024")  # Example date
        jumlah_input1.clear()
        jumlah_input1.send_keys("20000")
        sumber_input1.select_by_value("6")

        jumlah_input2 = self.driver.find_element(By.XPATH, "//input[@name='jumlah1']")
        sumber_input2 = Select(self.driver.find_element(By.XPATH, "//select[@name='sumber1']"))

        jumlah_input2.clear()
        jumlah_input2.send_keys("30000")
        sumber_input2.select_by_value("7")

        jumlah_input3 = self.driver.find_element(By.XPATH, "//input[@name='jumlah2']")
        sumber_input3 = Select(self.driver.find_element(By.XPATH, "//select[@name='sumber2']"))

        jumlah_input3.clear()
        jumlah_input3.send_keys("40000")
        sumber_input3.select_by_value("8")

        deskripsi_input1.clear()
        deskripsi_input1.send_keys("Pengeluaran untuk pakaian, skincare, dan transportasi")

        time.sleep(2)

        button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        time.sleep(2)

    def test_valid(self):
        self.login("yaya@gmail.com", "yaya12345")
        self.input_pengeluaran()

if __name__ == "__main__":
    unittest.main()

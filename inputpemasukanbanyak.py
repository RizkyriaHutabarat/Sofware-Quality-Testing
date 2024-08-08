import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SystemTest(unittest.TestCase):
    def setUp(self):
        # Initialize WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Add a delay before closing the WebDriver
        time.sleep(5)
        # Close the WebDriver
        self.driver.quit()

    def login(self, username, password):
        # Open login page
        self.driver.get("http://localhost/Money-Daily/LoginRegister.php")

        # Find username and password input elements by name attribute
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")

        # Enter username and password
        email_input.send_keys(username)
        password_input.send_keys(password)

        # Click login button
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".sign-in-form input[type='submit']")
        login_button.click()

        # Wait for page transition
        time.sleep(5)

    def input_pengeluaran(self, tgl_pemasukan, jumlah1, sumber1, jumlah2, sumber2, jumlah3, sumber3, deskripsi):
        self.driver.get("http://localhost/Money-Daily/pendapatan.php")
        
        # Wait until the modal dialog is visible
        tambah_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-success[data-target='#myModalTambah']"))
        )
        tambah_button.click()
        
        # Wait until the modal content is loaded
        tgl_pemasukan_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "tgl_pemasukan"))
        )
        # Clear any existing value and send keys in correct format "yyyy-mm-dd"
        tgl_pemasukan_input.clear()
        tgl_pemasukan_input.send_keys(tgl_pemasukan)

        jumlah_input1 = self.driver.find_element(By.NAME, "jumlah")
        jumlah_input1.send_keys(jumlah1)
        sumber_input1 = Select(self.driver.find_element(By.NAME, "sumber"))
        sumber_input1.select_by_value(sumber1)
        jumlah_input2 = self.driver.find_element(By.NAME, "jumlah1")
        jumlah_input2.send_keys(jumlah2)
        sumber_input2 = Select(self.driver.find_element(By.NAME, "sumber1"))
        sumber_input2.select_by_value(sumber2)
        jumlah_input3 = self.driver.find_element(By.NAME, "jumlah2")
        jumlah_input3.send_keys(jumlah3)
        sumber_input3 = Select(self.driver.find_element(By.NAME, "sumber2"))
        sumber_input3.select_by_value(sumber3)
        deskripsi_input = self.driver.find_element(By.NAME, "deskripsi")
        deskripsi_input.send_keys(deskripsi)
        
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        WebDriverWait(self.driver, 10).until(EC.url_contains("Money-Daily"))

    def test_system_flow(self):
        self.login("yaya@gmail.com", "yaya12345")
        self.input_pengeluaran("06/15/2024", "200000", "1", "150000", "2", "100000", "3", "Pengeluaran untuk berbagai keperluan")

if __name__ == "__main__":
    unittest.main()

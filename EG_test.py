# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from time import sleep
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

name = 'Anna'
lastname = 'Kowalska'
phone_number = '123123123'
street = 'Ptasia'
lot = '3'
apt = '9'
city = 'Pobierowo'
postal = '56-891'
valid_mail = 'ania@tlen.pl'
valid_password = 'jolka'
invalid_password = 'jelka'



class CzytamRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://czytam.pl/')


    def testWrongPassword(self):
        driver=self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-account"]/a[3]')))
        register=driver.find_element_by_xpath('//*[@id="header-account"]/a[3]')
        register.click()

        WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.NAME, 'imie')))
        name_input=driver.find_element_by_name('imie')
        name_input.send_keys(name)

        lastname_input=driver.find_element_by_name('nazwisko')
        lastname_input.send_keys(lastname)

        phone_number_input=driver.find_element_by_name('telefon')
        phone_number_input.send_keys(phone_number)

        adress_input=driver.find_element_by_name('ulica')
        adress_input.send_keys(street)

        lot_number_input=driver.find_element_by_name('nr_domu')
        lot_number_input.send_keys(lot)

        apartment_number_input=driver.find_element_by_name('nr_mieszkania')
        apartment_number_input.send_keys(apt)

        city_input=driver.find_element_by_name('miejscowosc')
        city_input.send_keys(city)

        postcode_input=driver.find_element_by_name('kod_pocztowy')
        postcode_input.send_keys(postal)

        adress_transfer=driver.find_element_by_id('przenies')
        adress_transfer.click()

        email_input=driver.find_element_by_name('email')
        email_input.send_keys(valid_mail)

        passwd_input=driver.find_element_by_name('haslo1')
        passwd_input.send_keys(valid_password)

        invpasswd_input=driver.find_element_by_name('haslo2')
        invpasswd_input.send_keys(invalid_password)

        terms_accept=driver.find_element_by_name('zgoda_regulamin')
        terms_accept.click()

        driver.find_element_by_xpath('//*[@id="panel-fizyczna"]/form/div[7]/input[2]').click()

        error_notice = driver.find_element_by_css_selector('#info_haslo1 > div')
        print(error_notice.text)
        self.assertEqual(error_notice.text, u"Hasło i powtórzenie muszą być identyczne\n×")

    def tearDown(self):
        self.driver.quit()



if __name__=='__main__':
    unittest.main(verbosity=2)

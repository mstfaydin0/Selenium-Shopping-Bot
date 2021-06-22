from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bilgiler import *
import time


class Satinal:
    driver = webdriver.Chrome("C:\\chromedriver.exe")
    driver.maximize_window()

    def signIn(self):
        self.driver.get("https://www.hepsiburada.com/uyelik/giris?ReturnUrl=https%3A%2F%2Fwww.hepsiburada.com%2F")
        time.sleep(3)
        usermailGir = self.driver.find_element_by_name("username")
        usermailGir.send_keys(mail)
        time.sleep(2)
        usersifreGir = self.driver.find_element_by_name("password")
        usersifreGir.send_keys(password)
        time.sleep(2)
        usersifreGir.send_keys(Keys.ENTER)
        time.sleep(4)

    def adresKayit(self):
        self.driver.get("https://www.hepsiburada.com/ayagina-gelsin/teslimat-adreslerim")
        time.sleep(3)
        self.driver.find_element_by_class_name("btn-add-new").click()
        time.sleep(2)
        self.driver.find_element_by_id("first-name").send_keys(isim)
        time.sleep(1)
        self.driver.find_element_by_id("last-name").send_keys(soyisim)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='form-address']/div/div/section[2]/div[3]/div/div/button").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//*[@id='form-address']/div/div/section[2]/div[3]/div/div/div/ul/li[37]/a").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='form-address']/div/div/section[2]/div[4]/div/div/button").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//*[@id='form-address']/div/div/section[2]/div[4]/div/div/div/ul/li[2]/a").click()
        time.sleep(1)
        self.driver.find_element_by_id("address").send_keys(adres)
        self.driver.find_element_by_id("address-name").send_keys("ev")
        self.driver.find_element_by_id("phone").send_keys(telno)
        time.sleep(1)
        self.driver.find_element_by_id("phone").send_keys(Keys.ENTER)

    def uruneGit(self):
        self.driver.get("https://www.hepsiburada.com/piem-kadin-siyah-ananas-t-shirt-p-HBV00000U3I6Z")
        time.sleep(1)
        self.driver.find_element_by_id("addToCart").click()
        time.sleep(1)

    def sepeteGit(self):
        self.driver.get("https://checkout.hepsiburada.com/sepetim")
        time.sleep(2)
        self.driver.find_element_by_id("continue_step_btn").click()
        time.sleep(1)
        self.driver.find_element_by_id("continue_step_btn").click()
        time.sleep(3)

    def odemeYap(self):
        self.driver.find_element_by_class_name("sardesPaymentPage-Accordion-accordion_tab").click()
        time.sleep(1)
        self.driver.find_element_by_name("cardNumber").send_keys(kartno)
        self.driver.find_element_by_name("holderName").send_keys(fullname)
        self.driver.find_element_by_name("expireDate").send_keys(skt)
        self.driver.find_element_by_name("cvv").send_keys(cvc)
        time.sleep(2)
        self.driver.find_element_by_id("continue_step_btn").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='agreement_check']/label/input").click()
        time.sleep(1)
        self.driver.find_element_by_id("continue_step_btn").click()


if __name__ == '__main__':
    satinal = Satinal()
    satinal.signIn()
    satinal.uruneGit()
    satinal.sepeteGit()
    satinal.odemeYap()

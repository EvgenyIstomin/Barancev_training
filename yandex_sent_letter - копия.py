# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
import unittest


class test_yandex_sent_letter (unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
    
    def test_yandex_sent_letter(self):
        self.login(username="istomin-e", password="IC!@hide#*")
        self.create_new_mail()
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_css_selector("div.mail-User-Name").click()
        wd.find_element_by_link_text("Выход").click()

    def fill_out_tema(self, tema):
        wd = self.wd
        wd.find_element_by_name("subj").click()
        wd.find_element_by_name("subj").clear()
        wd.find_element_by_name("subj").send_keys(tema)

    def fill_out_mail_address(self, email_address):
        wd = self.wd
        wd.find_element_by_name("to").click()
        wd.find_element_by_name("to").send_keys(email_address)

    def create_new_mail(self):
        wd = self.wd
        wd.find_element_by_link_text("Написать").click()
        self.fill_out_mail_address("istomin-e@yandex.ru")
        self.fill_out_tema("test")
        wd.find_element_by_id("nb-21").click()

    def login(self, username, password):
        wd = self.wd
        self.open_yandex_email_page()
        wd.find_element_by_name("login").click()
        wd.find_element_by_name("login").clear()
        wd.find_element_by_name("login").send_keys(username)
        wd.find_element_by_name("passwd").click()
        wd.find_element_by_name("passwd").clear()
        wd.find_element_by_name("passwd").send_keys(password)
        wd.find_element_by_xpath("//div[@class='new-left']//button[.='Войти']").click()

    def open_yandex_email_page(self):
        wd = self.wd
        wd.get("https://mail.yandex.ru/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

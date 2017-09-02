# -*- coding: utf-8 -*-
#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
import unittest

class test_yandex_search(unittest.TestCase):
    def setUp(self):
        #self.wd = webdriver.Chrome()
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_yandex_search(self):
        wd = self.wd
        wd.get("https://yandex.ru/")
        wd.find_element_by_id("text").click()
        wd.find_element_by_id("text").clear()
        wd.find_element_by_id("text").send_keys("webdriver")
        wd.find_element_by_xpath("//div[@class='search2__button']//button[.='Найти']").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

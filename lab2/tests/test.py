__author__ = 'mandriy'
# -*- coding: utf-8 -*-

import unittest
from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.common.keys import Keys
from test_utils import open_web_driver, PersonsLookerLifecycle
import os.path

class PersonsHunterMainFunctionality(unittest.TestCase):

    def main_functionality_test(self, web_driver):
        root = os.path.split(os.path.dirname(__file__))[0] + '/'
        data = [u'asfasf\n Шевченко Т. Г.', u'Шевченко А. Н.\n asfafa', u'Путин В. В.']
        with PersonsLookerLifecycle(data, root):
            with open_web_driver(web_driver) as driver:
                driver.get('http://localhost:8080')

    def test_in_Chrome(self):
        self.main_functionality_test(Firefox)

    def test_in_Firefox(self):
        self.main_functionality_test(Chrome)



__author__ = 'mandriy'
# -*- coding: utf-8 -*-

import unittest
from urls_dictionary.xml_works import parse_urls_xml


class TestXml(unittest.TestCase):

    def testReadValidXml(self):
        self.assertEqual(len(parse_urls_xml("test1_1.xml")), 2, 'Reading correct xml file.')

    def testReadInvalidXml(self):
        self.assertRaises(Exception, parse_urls_xml, "test1_2.xml",)

    def dictionary_printing(self):
        pass





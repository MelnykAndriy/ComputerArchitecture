__author__ = 'mandriy'
# -*- coding: utf-8 -*-

import unittest
from urls_dictionary.xml_works import *
import os


class TestXml(unittest.TestCase):

    def testReadValidXml(self):
        self.assertEqual(parse_urls_xml("test1_1.xml"),
                         ['https://pypi.python.org/pypi/pip/#downloads',
                          'http://docs.python-guide.org/'],
                         "Checks whether xml content was read properly.")

    def testReadInvalidXml(self):
        self.assertRaises(Exception, parse_urls_xml, "test1_2.xml",)

    def testDictionaryDumping(self):
        test_dict = {u'школяр': 2, u'директор': 4, u'товариш': 1}
        dump_occurrence_dict(test_dict, 'dump_test.xml')
        try:
            self.assertDictEqual(read_occurrence_dict('dump_test.xml'),
                                 test_dict,
                                 "Checks whether occurrence dictionary" +
                                 "is dumped correctly")
        finally:
            os.remove('dump_test.xml')

    def testDictionaryDumpingWithSorting(self):
        test_dict = {u'школяр': 2, u'директор': 4, u'товариш': 1}
        sorted_dict = {u'директор': 4, u'школяр': 2, u'товариш': 1}
        dump_occurrence_dict(test_dict, 'dump_test.xml', True)
        try:
            self.assertDictEqual(read_occurrence_dict('dump_test.xml'),
                                 sorted_dict,
                                 "Checks whether occurrence dictionary" +
                                 "is dumped in right order.")
        finally:
            os.remove('dump_test.xml')

__author__ = 'mandriy'
# -*- coding: utf-8 -*-


import unittest
from urls_dictionary.words_analyzes import ukrainian_converter


class WordsChecks(unittest.TestCase):

    def testStemGetting(self):
        self.assertEqual(ukrainian_converter(u'робітникові'), u'робітник', "checkStem 1")
        self.assertNotIn(False,
                         [ukrainian_converter(not_base_form) == u'сталевар'
                          for not_base_form in [u'сталевара', u'сталеварові', u'сталеваром']],
                         "checkStem 2")
__author__ = 'mandriy'
# -*- coding: utf-8 -*-


import unittest
from urls_dictionary.words_analyzes import ukrainian_converter


class WordsChecks(unittest.TestCase):

    def testStemGetting(self):
        self.assertEqual(ukrainian_converter('робітникові'), 'робітник', "checkStem 1")
        self.assertNotIn(False,
                         [ukrainian_converter(not_base_form) == 'сталевар'
                          for not_base_form in ['сталевара', 'сталеварові', 'сталеваром']],
                         "checkStem 2")
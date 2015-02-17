__author__ = 'mandriy'
# -*- coding: utf-8 -*-


import unittest
from urls_dictionary.words_analyzes import ukrainian_converter
from urls_dictionary.words_analyzes import make_occurrence_dictionary


class DictionaryWorks(unittest.TestCase):

    def testDictMaking(self):
        words = []
        words.extend([u'школярем', u'школярі'])
        words.extend([u'директор', u'директору',
                      u'директором', u'директорові'])
        words.extend([u'товаришу'])
        dictionary = make_occurrence_dictionary(words)
        msg = "Checks whether occurrence dictionary was built properly"
        self.assertDictEqual(dictionary, {u'школяр': 2,
                                          u'директор': 4,
                                          u'товариш': 1},
                             msg)


class WordsChecks(unittest.TestCase):

    def testStemGetting(self):
        self.assertEqual(ukrainian_converter(u'робітникові'),
                         u'робітник', "checkStem 1")
        self.assertNotIn(False,
                         [ukrainian_converter(not_base_form) == u'сталевар'
                          for not_base_form in [u'сталевара',
                                                u'сталеварові',
                                                u'сталеваром']],
                         "checkStem 2")
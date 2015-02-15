__author__ = 'mandriy'
# -*- coding: utf-8 -*-


import unittest
from urls_dictionary.words_analyzes import make_occurrence_dictionary


class DictionaryWorks(unittest.TestCase):

    def testDictMaking(self):
        words = []
        words.extend([u'школярем', u'школярі'])
        words.extend([u'директор', u'директору', u'директором', u'директорові'])
        words.extend([u'товаришу'])
        dictionary = make_occurrence_dictionary(words)
        self.assertDictEqual(dictionary, {u'школяр': 2, u'директор': 4, u'товариш': 1},
                             "Checks whether occurrence dictionary was built properly")

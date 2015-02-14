__author__ = 'mandriy'
# -*- coding: utf-8 -*-


import unittest
from urls_dictionary.words_analyzes import make_occurrence_dictionary


class DictionaryWorks(unittest.TestCase):

    def testDictMaking(self):
        words = []
        words.extend(['школярем', 'школярі'])
        words.extend(['директор', 'директору', 'директором', 'директорові'])
        words.extend(['товаришу'])
        dictionary = make_occurrence_dictionary(words)
        self.assertDictEqual(dictionary, {'школяр': 2, 'директор': 4, 'товариш': 1},
                             "Checks whether occurrence dictionary was built properly")

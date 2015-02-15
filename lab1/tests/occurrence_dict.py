__author__ = 'mandriy'
# -*- coding: utf-8 -*-


import unittest
from urls_dictionary.words_analyzes import make_occurrence_dictionary
from urls_dictionary.urls_processing import split_into_ukrainian_words, \
    ukrainian_words_from_urls


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

    def testTextSplitting(self):
        text = u'заселену вихідцями з цього регіону. У другій половині' + \
               u'XIX століття — початку XX століття, під впливом '
        self.assertEquals(split_into_ukrainian_words([text]),
                          [u'заселену', u'вихідцями', u'з', u'цього',
                           u'регіону', u'У', u'другій', u'половині',
                           u'століття', u'початку', u'століття', u'під',
                           u'впливом'])

    def testUrlWordsGetting(self):
        url = 'http://traditions.org.ua/viruvannia' \
              '/narodnyi-sonnyk/215-akvarium-sonnyk'
        words = ukrainian_words_from_urls([url])
        for word in words:
            words

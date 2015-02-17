__author__ = 'mandriy'
# -*- coding: utf-8 -*-


import unittest
import urls_dictionary.network_tools as network_tools
import urls_dictionary.urls_processing as urls_processing


class NetworkTests(unittest.TestCase):

    def testGeventLib(self):
        urls = [u'http://uk.wikipedia.org/wiki/Київ',
                u'http://uk.wikipedia.org/wiki/Азія']
        network_tools.set_net_lib('gevent')
        kiev_words = urls_processing.ukrainian_words_from_urls(urls[0:1])
        asia_words = urls_processing.ukrainian_words_from_urls(urls[1:2])
        all_words = len(urls_processing.ukrainian_words_from_urls(urls))
        self.assertEqual(
            all_words,
            len(kiev_words) + len(asia_words),
            "Gevent library approach.")

    def testStdLib(self):
        urls = [u'http://uk.wikipedia.org/wiki/Київ',
                u'http://uk.wikipedia.org/wiki/Азія']
        network_tools.set_net_lib('std')
        kiev_words = urls_processing.ukrainian_words_from_urls(urls[0:1])
        asia_words = urls_processing.ukrainian_words_from_urls(urls[1:2])
        self.assertEqual(
            len(urls_processing.ukrainian_words_from_urls(urls)),
            len(kiev_words) + len(asia_words),
            "Standard library approach.")

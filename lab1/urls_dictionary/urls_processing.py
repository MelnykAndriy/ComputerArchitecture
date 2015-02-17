__author__ = 'Andriy'

import re
import network_tools
from HTMLParser import HTMLParser

with_error_ignoring = True

special_ukrainian_letters = (u'\u0490', u'\u0491', u'\u0454', u'\u0456',
                             u'\u0457', u'\u0404', u'\u0406', u'\u0407')
special_russian_letters = (u'\u044A', u'\u044B', u'\u044D', u'\u0451',
                           u'\u042A', u'\u042B', u'\u042D', u'\u0401')
letters = tuple([unichr(i) for i in xrange(0x0410, 0x0450)])

ukr_letters = [letter for letter in letters
               if letter not in special_russian_letters]
ukr_letters.extend(special_ukrainian_letters)


def ukrainian_word_matcher():
    regex = u"[%s]+" % reduce(lambda x, y: x+y, ukr_letters)
    return re.compile(regex, re.UNICODE)


class UkrainianWordsCollector(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.__words__ = None
        self.__spliter__ = ukrainian_word_matcher()

    def collect(self, html_text):
        self.__words__ = []
        self.feed(html_text)
        words = self.__words__[:]
        return words

    def handle_data(self, data):
        self.__words__.extend(self.__spliter__.findall(data))


def error_logger(log_func, *log_func_params):
    try:
        return log_func(*log_func_params)
    except Exception as exc:
        print exc.message
        if not with_error_ignoring:
            raise exc


def ukrainian_words_from_urls(urls_to_process):
    def url_text_processor(html_text):
        words_collector = UkrainianWordsCollector()
        return words_collector.collect(html_text)

    return reduce(lambda all_words, url_words:
                  all_words + url_words,
                  filter(
                      lambda x: x is not None,
                      network_tools.map_urls_sources(url_text_processor,
                                                     urls_to_process,
                                                     error_logger)),
                  [])

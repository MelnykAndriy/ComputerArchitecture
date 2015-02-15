__author__ = 'mandiy'
# -*- coding: utf-8 -*-

import hunspell
from os import getenv


class Converter:

    def __init__(self, hunspell_dictionary):
        self.dictionary = hunspell_dictionary

    def __call__(self, word):

        stem_res = map(lambda base_word: unicode(base_word, 'UTF-8'),
                       self.dictionary.stem(word))
        if stem_res:
            if word in stem_res:
                return word
            return stem_res[0]
        else:
            return None

try:
    ukrainian_converter = Converter(hunspell.HunSpell(
        getenv("LAB1_DICTIONARY_PATH") + '/uk_UA.dic',
        getenv("LAB1_DICTIONARY_PATH") + '/uk_UA.aff'))
except:
    raise Exception("Must supply a path to uk_UA.aff and uk_UA.dic in " +
                    "the environment variable LAB1_DICTIONARY_PATH.")


def make_occurrence_dictionary(words):
    ret_dic = dict()
    for word in words:
        base_form = ukrainian_converter(word)
        if base_form:
            if ret_dic.get(base_form):
                ret_dic[base_form] += 1
            else:
                ret_dic[base_form] = 1
    return ret_dic
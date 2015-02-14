__author__ = 'mandiy'

import hunspell
from os import getenv


class Converter:

    def __init__(self, hunspell_dictionary):
        self.dictionary = hunspell_dictionary

    def __call__(self, word):
        return self.dictionary.stem(word)[0]


try:
    ukrainian_converter = Converter(hunspell.HunSpell(getenv("LAB1_DICTIONARY_PATH") + '/uk_UA.dic',
                                                      getenv("LAB1_DICTIONARY_PATH") + '/uk_UA.aff'))
except:
    raise Exception("Must supply a path to uk_UA.aff and uk_UA.dic in " +
                    "the environment variable LAB1_DICTIONARY_PATH.")


def make_occurrence_dictionary(words):
    ret_dic = dict()
    for word in map(ukrainian_converter, words):
        if ret_dic.get(word):
            ret_dic[word] += 1
        else:
            ret_dic[word] = 1
    return ret_dic
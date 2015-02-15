__author__ = 'Andriy'

import re
from network_tools import url_to_tree


special_ukrainian_letters = (u'\u0490', u'\u0491', u'\u0454', u'\u0456',
                             u'\u0457', u'\u0404', u'\u0406', u'\u0407')
special_russian_letters = (u'\u044A', u'\u044B', u'\u044D', u'\u0451',
                           u'\u042A', u'\u042B', u'\u042D', u'\u0401')
letters = tuple([unichr(i) for i in xrange(0x0410, 0x0450)])

ukr_letters = [letter for letter in letters
               if letter not in special_russian_letters]
ukr_letters.extend(special_ukrainian_letters)


def ukrainian_words_from_urls(urls_to_process):
    return reduce(lambda words, url:
                  words + split_into_ukrainian_words(url_text_pieces(url)),
                  urls_to_process,
                  [])


def split_into_ukrainian_words(list_of_text_pieces):
    spliter = re.compile(u"[%s]+" % reduce(lambda x, y: x+y, ukr_letters),
                         re.UNICODE)
    return reduce(lambda words, text_piece: words+spliter.findall(text_piece),
                  list_of_text_pieces, [])


def url_text_pieces(url):
    def tree_traverse(node):
        return reduce(lambda texts, subnode: texts + tree_traverse(subnode),
                      node,
                      filter(lambda text: text is not None, [node.text]))
    try:
        return tree_traverse(url_to_tree)
    except:
        print "Can't process url %s properly." % url,

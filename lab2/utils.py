__author__ = 'mandriy'

from xml.etree import ElementTree
from xml.dom import minidom
import os
import sys
from os.path import isdir, exists, join


def set_server_root(path):
    sys.path.append(os.path.dirname(os.path.abspath(path)))
    os.chdir(os.path.dirname(path))


def get_files(path):
    def travers_files(p, func):
        if isdir(p):
            return reduce(lambda files, file_or_dir:
                          files + travers_files(join(p, file_or_dir), func),
                          os.listdir(p),
                          [])
        else:
            return [func(p)]

    def read_file(filename):
        with open(filename, "r") as f:
            return f.read().decode('utf-8')

    if exists(path):
        return travers_files(path, read_file)
    else:
        return []


def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ").encode('utf-8')


normalized_dict = {ord(u'"'): u'', ord(u'\\'): u''}
for i in xrange(32):
    normalized_dict[i] = u''


def normalize_text_for_json(text):
    return text.translate(normalized_dict)

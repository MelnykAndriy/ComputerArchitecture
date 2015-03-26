__author__ = 'mandriy'

from xml.etree import ElementTree
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ").encode('utf-8')


normalized_dict = {ord(u'"'): u' '}
for i in xrange(32):
    normalized_dict[i] = u' '


def normalize_text_for_json(text):
    return text.translate(normalized_dict)

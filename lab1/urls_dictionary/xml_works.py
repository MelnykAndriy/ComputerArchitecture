__author__ = 'Andriy'

from xml.etree.ElementTree import parse
from xml.etree import ElementTree
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")


def parse_urls_xml(urls_xml):
    xml_root = parse(urls_xml).getroot()
    if xml_root.tag != "urls_dictionary":
        raise Exception("Invalid xml structure.")
    return [url.text for url in xml_root.iter('url')]


def dump_dict(dict_to_dump, xml_file):
    root = ElementTree.Element("occurrence_dictionary")
    for word, occurrence_number in dict_to_dump.items():
        word_record = ElementTree.SubElement(root, "word_record")
        word_subelem = ElementTree.SubElement(word_record, "word")
        occurrence_number_subelem = ElementTree.SubElement(word_record, "occurrence_number")
        word_subelem.text, occurrence_number_subelem.text = word, str(occurrence_number)
    f = open(xml_file, "w")
    f.write(prettify(root))
    f.close()




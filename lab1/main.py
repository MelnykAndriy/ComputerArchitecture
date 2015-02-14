__author__ = 'Andriy'

import argparse
from urls_dictionary.xml_works import dump_dict
from urls_dictionary.urls_processing import process_urls

args_parser = argparse.ArgumentParser(version='1.0', add_help=True)

args_parser.add_argument('-urls_dictionary', action='store', dest='urls_dictionary', help='XML file with urls_dictionary which will be analyzed.')
args_parser.add_argument('-res', action='store', dest='result', help='Path to result file.')




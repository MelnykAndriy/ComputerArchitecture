__author__ = 'Andriy'

import argparse
from urls_dictionary.xml_works import dump_dict
# from urls_dictionary.urls_processing import process_urls

args_parser = argparse.ArgumentParser(version='1.0', add_help=True)

args_parser.add_argument('-urls', action='store', dest='urls_dictionary', help='XML file with list of urls' +
                                                                               'which will be analyzed.')
args_parser.add_argument('-res', action='store', dest='result', help='Path to result file.')
args_parser.add_argument('-netlib', action='store', dest='netlib', help='Configures which library will be used for' +
                                                                        ' internet access.\n' +
                                                                        ' Two values are possible : gevent or std.\n')





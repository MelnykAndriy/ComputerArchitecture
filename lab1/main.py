__author__ = 'Andriy'

import argparse
import ConfigParser
import sys
from urls_dictionary.network_tools import set_net_lib
from urls_dictionary.xml_works import dump_dict, parse_urls_xml
from urls_dictionary.words_analyzes import make_occurrence_dictionary
from urls_dictionary.urls_processing import ukrainian_words_from_urls

args_parser = argparse.ArgumentParser(version='1.0',
                                      add_help=True,
                                      prog='lab1',
                                      description='Traverses provided urls' +
                                                  ' and build' +
                                                  ' occurrence dictionary.')

args_parser.add_argument('urls_files', metavar='urls-files',
                         type=str, nargs='+',
                         help='XML files with list of urls' +
                              'which will be analyzed.')
args_parser.add_argument('-res', action='store', dest='result',
                         help='Path to result file.',
                         default='lab1_result.xml')

configfile = 'lab1.cfg'

config = ConfigParser.RawConfigParser({'net_lib': 'std'})
config.read(configfile)
parsed_args = args_parser.parse_args(sys.argv)

if config.has_section('Network tools') and \
        config.has_option('Network tools', 'lib'):
    set_net_lib(config.get('Network tools', 'lib'))
else:
    set_net_lib(config.defaults().get('net_lib'))


dump_dict(
    make_occurrence_dictionary(
        ukrainian_words_from_urls(
            reduce(lambda urls, urls_file: urls + parse_urls_xml(urls_file),
                   parsed_args.urls_files,
                   []))),
    parsed_args.result, True)

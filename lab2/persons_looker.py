__author__ = 'mandriy'


from server import *
import argparse

args_parser = argparse.ArgumentParser(version='1.0',
                                      add_help=True,
                                      prog='lab1',
                                      description='')


args_parser.add_argument('path', metavar='path',
                         type=str, nargs='+',
                         help='Path to directory or file which should be analyzed.')

args_parser.add_argument('-n', action='store', dest='cluster_number',
                         help='Path to result file.',
                         default='lab1_result.xml')

args_parser.add_argument('-b', action='store', dest='')


run_server()

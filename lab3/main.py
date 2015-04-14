__author__ = 'mandriy'

import argparse
import sys
import threading


args_parser = argparse.ArgumentParser(version='1.0',
                                      add_help=True,
                                      prog='lab3',
                                      description='Provides an interface for couch db.')

args_parser.add_argument('-s', '--soap',
                         action='store_true',
                         dest='soap',
                         help='Starts a soap service.')
args_parser.add_argument('-r', '--rest',
                         action='store_true',
                         dest='rest',
                         help='Starts a rest server.')

args = args_parser.parse_args(sys.argv)

soap_thread = threading.Thread(target=lambda: args.soap and None)
rest_thread = threading.Thread(target=lambda: args.rest and None)

soap_thread.start()
rest_thread.start()

soap_thread.join()
rest_thread.join()

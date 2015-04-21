__author__ = 'mandriy'

import argparse
import sys
import multiprocessing
import soap_couchDB_iface.service as soap_service
import rest_couchDB_iface.server as rest_server
import signal

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

args = args_parser.parse_args(sys.argv[1:])

soap_thread = multiprocessing.Process(target=lambda: args.soap and soap_service.ProgrammersAccessSoapServer.start())
rest_thread = multiprocessing.Process(target=lambda: args.rest and rest_server.run_rest_server())

soap_thread.start()
rest_thread.start()

print '\nProgrammers couchdb accessor welcomes you.'
print 'Press Ctrl+C to stop hosting.'


def sigint_handler(*_):
    if soap_thread.is_alive():
        soap_thread.terminate()
    if rest_thread.is_alive():
        rest_thread.terminate()

signal.signal(signal.SIGINT, sigint_handler)
signal.pause()



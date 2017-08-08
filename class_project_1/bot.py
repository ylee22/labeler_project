#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script will respond to a greeting from the command line.

Run `python setup.py install` to install the command 'bot'.

A typical interaction with this bot would be:

$ bot Hi
$ Hi person. How are you?
"""
from __future__ import division, print_function, absolute_import

import argparse
import sys
import logging

from class_project_1 import __version__

__author__ = "Yerim Lee"
__copyright__ = "Yerim Lee"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def recognize_greeting(statement):
    """Recognizes if string statement starts with Hi or Hey or any other greeting,

    Args:
        statement (str): a string from the commandline from the user

    Returns:
        bool: True if statement is a greeting. False otherwise.

    # >>> recognize_greeting('hi'):
    True
    """
    statement = statement.lower()
    if statement.startswith('hi') or statement.startswith('hey'):
        return True
    return False


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    return None, args
    parser = argparse.ArgumentParser(
        description="Just a greeting recognizer")
    # parser.add_argument(
    #     '--version',
    #     action='version',
    #     version='class_project_1 {ver}'.format(ver=__version__))
    # # parser.add_argument(
    # #     dest="n",
    # #     help="n-th Fibonacci number",
    # #     type=int,
    # #     metavar="INT")
    # parser.add_argument(
    #     '-v',
    #     '--verbose',
    #     dest="loglevel",
    #     help="set loglevel to INFO",
    #     action='store_const',
    #     const=logging.INFO)
    # parser.add_argument(
    #     '-vv',
    #     '--very-verbose',
    #     dest="loglevel",
    #     help="set loglevel to DEBUG",
    #     action='store_const',
    #     const=logging.DEBUG)
    return parser.parse_known_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args, unknown = parse_args(args)
    # setup_logging(args.loglevel)
    # _logger.debug("Starting crazy calculations...")
    print("{}".format(recognize_greeting(' '.join(unknown))))
    # _logger.info("Script ends here")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()

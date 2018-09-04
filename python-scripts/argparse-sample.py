

# argparse — Parser for command-line options, arguments and sub-commands
# https://docs.python.org/3/library/argparse.html

import argparse

"""
   1 Require a filename argument, so it knows what file to read.
   2 Print the contents of the file backward (bottom of the script first, each line printed backward)
   3 Provide help text and documentation when it receives the --help flag.
   4 Accept an optional --limit or -l flag to specify how many lines to read from the file.
   5 Accept a --version flag to print out the current version of the tool.
"""

# build the parser 
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to read')

# parse the arguments 
args = parser.parse_args()
# read the file reverse the contents and print 

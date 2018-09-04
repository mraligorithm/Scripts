

# argparse — Parser for command-line options, arguments and sub-commands
# https://docs.python.org/3/library/argparse.html

import argparse
import sys

"""
   1 Require a filename argument, so it knows what file to read.
   2 Print the contents of the file backward (bottom of the script first, each line printed backward)
   3 Provide help text and documentation when it receives the --help flag.
   4 Accept an optional --limit or -l flag to specify how many lines to read from the file.
   5 Accept a --version flag to print out the current version of the tool.
"""

# build the parser 
parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')


# parse the arguments 
args = parser.parse_args()
print(args)

# handle the error     https://docs.python.org/3/reference/compound_stmts.html#the-try-statement
try:
    f = open(args.filename)
    limit = args.limit 
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(2)
except:
    print('Error occured')
else:
    # read the file reverse the contents and print 
    with open(args.filename) as f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:args.limit]

        for line in lines:
            print(line.strip()[::-1])
finally:
    print('Script Done')
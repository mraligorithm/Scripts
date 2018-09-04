

import argparse
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial (or complete) string to search for in words')

args = parser.parse_args()
snippet = args.snippet.lower()

with open('/usr/share/dict/words') as f:
  words = f.readlines()

matches = []

for word in words:
   if snippet in word.lower():
       matches.append(word)
print(matches)

words = open('/usr/share/dict/words').readlines()
print([word for word in words if snippet in word.lower()])

# words = open('/usr/share/dict/words').readlines()
# print([word.strip() for word in words if snippet in word.lower()])

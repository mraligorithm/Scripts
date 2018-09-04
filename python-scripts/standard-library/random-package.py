import random # https://docs.python.org/3/library/random.html
import os # https://docs.python.org/3/library/stdtypes.html#range
import json # https://docs.python.org/3/library/json.html

count = int(os.getenv("FILE_COUNT") or 100)
words = [word.strip() for word in open ('/user/share/dict/words').readlines()]

for indentifier in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
        'topic': random.choice(words),
        'value': "%2f" % amount
    }

    with open(f'./new/receipt-{identifier}.json', 'w') as f:
        json.dump(content, f)

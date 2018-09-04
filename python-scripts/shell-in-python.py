# Execute shell commands in python
import subprocess
# https://docs.python.org/3/library/subprocess.html


proc = subprocess.run(
    ['ls', '-l'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    )
# Typed version of the return of open() in text mode.
from typing import TextIO
# Text I/O implementation using an in-memory buffer.
from io import StringIO

input_string = '1.3 3.4\n2 4.2\n-1 1\n'
# print(input_string)

infile = StringIO(input_string)
print(infile.readline())
infile.readline()
print(infile.readline())
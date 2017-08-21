#coding: utf-8
"""
   sort birth dict
   read from stdin, output to stdout
   output order: 90s>80s>00s>other
"""
from sys import stdin
y_90 = []
y_80 = []
y_00 = []
other = []
line = stdin.readline()
while line:
    line = line[:-1]
    if len(line) == 8:
        char = line[2]
        if char == '9':
            y_90.append(line)
        elif char == '8':
            y_80.append(line)
        elif char == '0':
            y_00.append(line)
        else:
            other.append(line)
    elif len(line) == 6:
        char = line[0]
        if char == '9':
            y_90.append(line)
        elif char == '8':
            y_80.append(line)
        elif char == '0':
            y_00.append(line)
        else:
            other.append(line)
    else:
        other.append(line)
    line = stdin.readline()
for s in y_90:
    print s
for s in y_80:
    print s
for s in y_00:
    print s
for s in other:
    print s

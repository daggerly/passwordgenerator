#coding: utf-8
"""
   sort name dict
   read from stdin, output to stdout
   output order: all lower -- aaa
                 capital upper -- Aaa
                 all upper -- AAA
                 other -- aAA 
"""
from sys import stdin
lower = []
capital = []
upper = []
other = []
line = stdin.readline()
while line:
    line = line[:-1]
    if line.islower():
        lower.append(line)
    elif line.isupper():
        upper.append(line)
    elif line[0].isupper() and line[1].islower():
        capital.append(line)
    else:
        other.append(line)
    line = stdin.readline()
for s in lower:
    print s
for s in capital:
    print s
for s in upper:
    print s
for s in other:
    print s

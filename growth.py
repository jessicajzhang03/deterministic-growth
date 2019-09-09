import numpy as np
from collections import Counter
import itertools
from operator import add
import pprint as pp

UPGRADE = [(0,1),(0,-1),(1,0),(-1,0)]

def x(n):
    if not n:
        return [set([(0,0)])]
    prev = x(n-1)
    total = set.union(*prev)
    c = Counter(tuple(map(add,i[0],i[1])) for i in itertools.product(total,UPGRADE))
    added = set(x for x in c if c[x]==1 and x not in total)
    return prev + [added]

f = open('size_tables.txt','w')
n = 128
up_to_n = x(n)
total = 0
f.write('u(i) and U(i) for i between 0 and {}\n'.format(n))
n = 0
for exactly_n in up_to_n:
    add = len(exactly_n)
    total += add
    spaces = ' '*(8 - len(str(add)))
    spaces2 = ' '*(8 - len(str(total)))
    binary = bin(n)[2:]
    f.write('{}{}{}{}{}\n'.format(add,spaces,total,spaces2,binary))
    n += 1
f.close()

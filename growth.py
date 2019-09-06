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

f = open('size_of_An.txt','w')
g = open('size_of_Xn.txt','w')
n = 128
up_to_n = x(n)
total = 0
f.write('Size of X_i - X_(i+1) for i between 1 and {}\n'.format(n))
f.write('Size of X_i for i between 1 and {}\n'.format(n))
for exactly_n in up_to_n:
    total += len(exactly_n)
    f.write(str(len(exactly_n))+'\n')
    g.write(str(total)+'\n')
f.close()
g.close()
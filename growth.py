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

with open('size_of_An.txt','w') as f:
    n = 128
    up_to_n = x(n)
    f.write('Size of X_i - X_(i+1) for i between 1 and {}\n'.format(n))
    for exactly_n in up_to_n:
        f.write(str(len(exactly_n))+'\n')
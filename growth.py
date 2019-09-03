import math 
from collections import Counter
import pprint as pp

upgrade = set([(0,1),(1,0),(0,-1),(-1,0)])

def points_up_to(n):
    if not n:
        return set([(0,0)])
    prev = points_up_to(n-1)
    c = Counter((i[0]+j[0],i[1]+j[1]) for i in prev for j in upgrade)
    added = [x for x in c if c[x]==1]
    return prev.union(added)

# def points_first_in(n):
#     if not n:
#         return set([0,0])
#     prev = points_up_to(n-1)
#     c = Counter((i[0]+j[0],i[1]+j[1]) for i in prev for j in upgrade)
#     added = [x for x in c if c[x]==1]
#     return added

pp.pprint(points_up_to(5))
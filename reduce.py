#!/usr/bin/env python 

import sys
from itertools import groupby
from operator import itemgetter

def read_map_op(file):
        for line in file:
                yield line.strip().split('\t')

data = read_map_op(sys.stdin)

for row,group in groupby(data, itemgetter(0)):
    #print(row)

    list= " ".join([item[1][2] for item in group])
    print (row+'\t'+list)

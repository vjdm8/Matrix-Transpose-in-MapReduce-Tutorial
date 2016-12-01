#!/usr/bin/env python 

import sys

for line in sys.stdin:
    #print line
    line=line.strip()#remove side spaces
    words=line.split('\t')# split rownumber, values
    #print words
    rownum=words[0]
    #print rownum


    words2=words[1].strip().split(' ')#remove side spaces and split values
    #print words2
    #print len(words2)

    #loop through values
    numofcols=len(words2)
    for i in range(numofcols):
        print('{0}\t{1},{2}'.format(i,rownum,words2[i]))

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    seqList = []
    for i in range(n):
        seqList.append([])
    lastAnswer = 0
    for query in queries:
        if query[0] == 1:
            seqIndex = (query[1] ^ lastAnswer) % n
            seqList[seqIndex].append(query[2])
        if query[0] == 2:
            seqIndex = (query[1] ^ lastAnswer) % n
            lastAnswer = seqList[seqIndex][query[2] % len(seqList[seqIndex])]
            fptr.write(str(lastAnswer) + '\n')
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    dynamicArray(n, queries)

    fptr.close()

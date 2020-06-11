#!/bin/python3

import os
import sys
import functools

def simpleArraySum(ar):
    sumArr = functools.reduce(lambda a,b: a+b, ar)
    return sumArr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

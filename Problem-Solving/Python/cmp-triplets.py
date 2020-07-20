#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    pointA, pointB = 0,0
    for score in range(len(a)):
            if a[score] > b[score]:
                pointA = pointA +1
            if b[score] > a[score]:
                pointB = pointB + 1
        
    points = [pointA, pointB]
    return points

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

def hourglass_sum(arr, r, c):
    return arr[r][c] + arr[r][c+1] + arr[r][c+2] +\
     arr[r+1][c+1] + arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2]

if __name__ == '__main__':
    arr = []
    max_sum = -sys.maxsize -1

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    for r in range(0, len(arr) - 2):
        for c in range (0, len(arr[0]) - 2):
            curr_sum = hourglass_sum(arr, r, c)
            max_sum = max(curr_sum, max_sum)
    print(max_sum)

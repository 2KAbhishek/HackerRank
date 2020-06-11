import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binaryN = bin(n)
    binStr = str(binaryN)
    binStr = binStr[2:]
    consecList = [0]
    count = 1

    for i in range(len(binStr) - 1):
        if binStr[i] == binStr[i+1]:
            count += 1
        else:
            consecList.append(count)
            count = 1
    if (count >= max(consecList)):
        print(count)
    else:
        print(max(consecList))

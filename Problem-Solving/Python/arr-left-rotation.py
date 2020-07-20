#!/bin/python3

if __name__ == '__main__':
    nd = input().split()

    length = int(nd[0])

    rotate = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    if rotate > length:
        rotate %= length
    
    arr = arr[rotate:] + arr[0:rotate]
    
    for num in arr:
        print(num,end=" ")

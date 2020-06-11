n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swaps = 0

for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swaps += 1
    if not swaps:
        break


print('Array is sorted in '+str(swaps)+' swaps.')
print('First Element: '+str(a[0]))
print('Last Element: '+str(a[-1]))
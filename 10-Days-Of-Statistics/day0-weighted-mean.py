count = int(input())

nums = list(map(int, input().split()))
weights = list(map(int, input().split()))

sum_Nums = sum([a*b for a,b in zip(nums,weights)])
print(round((sum_Nums/sum(weights)),1))

# import numpy as np

# print (np.average(nums, weights))


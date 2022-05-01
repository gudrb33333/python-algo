#n개 페어를 이용하여 min(a, b)의 합으로 만들수 있는 가장 큰수를 만들어라.

import itertools

nums: list[int] = [1, 4, 3, 2]

nCr: list = itertools.combinations(nums, 2)
n: int = len(nums)//2
sumDic = {}

for item in nCr:
  sumDic[min(item)] = item

print(sumDic)

sumDic = sorted(sumDic.keys())
print(sumDic)
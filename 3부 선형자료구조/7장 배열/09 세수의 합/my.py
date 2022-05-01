import itertools
import time
start = time.time()

nums: list[int] = [-1, 0, 1, 2, -1, -4]

sumList: list = []

nPr: list = itertools.combinations(nums, 3)

for item in nPr:
  if(sum(item) == 0):
      sumList.append(list(item))

print(sumList)

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
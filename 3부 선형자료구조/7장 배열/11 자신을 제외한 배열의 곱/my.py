#배열을 입력받아 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라
from functools import reduce
from collections import deque

import time
start = time.time()

nums: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result: list = []
temp: int = 0

dq = deque(nums)

for num in nums:
  temp = dq.popleft()
  result.append(reduce(lambda acc, cur: acc * cur, dq))
  dq.append(temp)

print(result)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
nums: list[int] = [1, 4, 3, 2]

test = [2, 3, 5, 1]
print(min(test))

sum = 0
pair = []
nums.sort()

for n in nums:
  pair.append(n)
  if len(pair) == 2:
    sum += min(pair)
    pair = []


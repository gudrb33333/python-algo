import itertools

#덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

nums: list[int] = [2, 7, 15 ,11]
target: int = 9

dict = {}

for i, num in enumerate(nums):
    dict[num] = i

print(dict)

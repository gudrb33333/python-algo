import itertools

#덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

nums: list[int] = [2, 7, 11 ,15]
target: int = 9

for i,n in enumerate(nums):
    print(nums[i + 1:])



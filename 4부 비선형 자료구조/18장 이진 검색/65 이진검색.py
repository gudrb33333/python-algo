import bisect

nums = [-1, 0, 3, 5, 9, 12]
target = 9

index = bisect.bisect_right(nums, target)

if index < len(nums) and nums[index] == target:
    print(index)
else:
    print(-1)
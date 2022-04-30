nums: list[int] = [2, 7, 11, 15]
target: int = 33

def twoSum(nums: list[int], target: int) -> list[int]:
  left,right = 0, len(nums) - 1

  while not left == right:
    if nums[left] + nums[right] < target:
      left += 1
    elif nums[left] + nums[right] > target:
      right -= 1
    else:
      return [left, right]
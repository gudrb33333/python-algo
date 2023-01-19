import itertools

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        for i in nums:
            combination_list = list(itertools.combinations(nums, i))
            result.append(combination_list)

        print(result)


nums=[1,2,3]
test = Solution()
test.subsets(nums)
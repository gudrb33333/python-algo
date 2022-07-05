from unittest import result


class Solution:  
    result = []

    def dsf(self, limit: int, depth: int, temp_result: list[int], nums: list[int] ):
        if depth == limit:
            self.result.append(temp_result)
            return

        for num in nums:
            self.dsf(limit, depth + 1, temp_result, nums)


    def permute(self, nums: list[int]) -> list[list[int]]:
        limit = len(nums)
        depth = 0
        temp_result = []
        
        self.dsf(limit, depth, temp_result, nums)
        return self.result
        


nums = [1,2,3]
test = Solution()

test.permute(nums)

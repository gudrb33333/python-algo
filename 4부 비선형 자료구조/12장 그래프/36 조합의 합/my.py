import itertools 

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def dfs(candidates: list[int], target: int, path: list[int]):
            if sum(path) > target:
                return
            if sum(path) == target:
                result.append(path)
                print(result)
                return

            for index, item in enumerate(candidates):
                dfs(candidates, target, path + [candidates[index]])
        
        dfs(candidates, target, [])

candidates = [2,3,6,7]
target = 7

test = Solution()
print(test.combinationSum(candidates, target))


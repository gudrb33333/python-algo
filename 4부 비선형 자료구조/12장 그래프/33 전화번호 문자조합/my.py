class Solution:
    dict = { 2:"abc" , 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tub", 9:"wxyz" }

    def dfs(self, result: list[str], depth: int, limit: int, str_temp: str):
        if depth == limit:
            result.append(str_temp)
            return    

        for char in self.dict[int(digits[depth])]:
            self.dfs( result, depth + 1, limit ,str_temp + char)

    def letterCombinations(self, digits: str) -> list[str]:
        result = []
        str_temp = ""
        depth = 0
        limit = len(digits)
        if limit < 0 :
            return self.result

        self.dfs(result, depth, limit ,str_temp)

        return result


digits = "23"

test = Solution()

print(test.letterCombinations(digits))

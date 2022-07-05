from itertools import count


class Solution:
    def dfs(self, grid: list[list[str]], row: int, column: int):
        if(column < 0 or column >= len(grid[0]) or row < 0 or row >= len(grid)):
            return

        grid[row][column] = '#'

        #동서남북 체크
        self.dfs(grid, row, column+1)
        self.dfs(grid, row, column-1)
        self.dfs(grid, row+1, column)
        self.dfs(grid, row-1, column)    

    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        count = 0

        for row in len(grid):
            for column in len(grid[0]):
                if grid[row][column] == '1':
                    self.dfs(row, column)
                    count += 1
        
        return count


grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]



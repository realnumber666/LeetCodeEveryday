class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)  # 行数
        n = len(grid[0])  # 列数
        # 1. 生成第一行第一列的值
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        # 2. 生成其余的值
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]
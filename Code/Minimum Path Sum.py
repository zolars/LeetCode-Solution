# Minimum Path Sum


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                print i, j
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[0][j] += grid[0][j - 1]
                elif j == 0:
                    grid[i][0] += grid[i - 1][0]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return(grid[-1][-1])


if __name__ == '__main__':
    print(Solution().minPathSum(
        [
            [1, 2, 3, 4, 5],
            [9, 8, 34, 6, 2],
            [23, 4, 5, 3, 5]
        ]
    ))

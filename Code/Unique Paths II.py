# Unique Paths II


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = []
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                print i, j, obstacleGrid[i][j]
                if obstacleGrid[i][j]:
                    obstacleGrid[i][j] = -1
            dp.append([0] + obstacleGrid[i])

        dp = [[0] * (len(obstacleGrid[0]) + 1)] + dp
        dp[0][1] = 1

        print dp

        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if dp[i][j] != -1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

                if dp[i][j] < 0:
                    dp[i][j] = 0

        print dp
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))

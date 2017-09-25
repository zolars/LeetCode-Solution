class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        dp = [0 for i in xrange(n)]
        dp[0], dp[1] = 1, 2

        for i in xrange(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]


if __name__ == '__main__':
    print(Solution().climbStairs(200))

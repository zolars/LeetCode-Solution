# Unique Binary Search Trees


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]
        for i in xrange(1, n + 1):
            dp.append(0)
            for j in xrange(i):
                dp[-1] += dp[j] * dp[i - j - 1]
        return dp[-1]


if __name__ == '__main__':
    print Solution().numTrees(50)

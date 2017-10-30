# Distinct Subsequences


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0 for j in xrange(len(s) + 1)] for i in xrange(len(t) + 1)]
        for i in xrange(len(dp[0])):
            dp[0][i] = 1

        for i in xrange(len(t)):
            temp = 0
            for j in xrange(len(s)):
                if t[i] == s[j]:
                    temp += dp[i][j]
                dp[i + 1][j + 1] += temp

        return dp[-1][-1]


if __name__ == '__main__':
    print Solution().numDistinct("", "")

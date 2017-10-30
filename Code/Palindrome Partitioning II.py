# Palindrome Partitioning II


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        mincut = [len(s) - i - 1 for i in xrange(len(s) + 1)]

        dp = [[False for i in xrange(len(s))] for j in xrange(len(s))]

        for i in reversed(xrange(0, len(s))):
            for j in xrange(i, len(s)):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    mincut[i] = min(mincut[i], mincut[j + 1] + 1)

        for i in xrange(len(dp)):
            for j in xrange(len(dp[i])):
                if dp[i][j]:
                    print s[i:j + 1]

        return mincut[0]


if __name__ == '__main__':
    print Solution().minCut("aab")

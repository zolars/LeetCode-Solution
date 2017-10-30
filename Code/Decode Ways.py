# Decode Ways


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or s[0] == "0":
            return 0
        if len(s) == 1:
            return 1

        dp = [0 for _ in xrange(len(s))] + [1]

        for i in reversed(xrange(len(s))):

            if i == len(s) - 1 and s[i] != "0":
                dp[i] = dp[i + 1]
                continue

            if s[i] == "0":
                dp[i] = 0
                continue

            temp = int(s[i] + s[i + 1])

            if 0 < temp < 27:
                dp[i] = dp[i + 1] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]

        return dp[0]


if __name__ == '__main__':
    print Solution().numDecodings("123456")

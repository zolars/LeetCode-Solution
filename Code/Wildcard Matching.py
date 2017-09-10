# Wildcard Matching


class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        length = len(s)
        if len(p) - p.count('*') > length:
            return False

        dp = [True] + [False] * length
        print dp
        for i in p:
            if i != '*':
                for j in reversed(range(length)):
                    dp[j + 1] = dp[j] and (i == s[j] or i == '?')
            else:
                for j in range(1, length + 1):
                    dp[j] = dp[j - 1] or dp[j]

            dp[0] = dp[0] and i == '*'
            print dp
        return dp[-1]


if __name__ == '__main__':
    print Solution().isMatch("bbddaaa", "*a*a*")

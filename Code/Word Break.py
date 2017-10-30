# Word Break


class Solution(object):
    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s == "":
            return True

        for i in wordDict:
            if s[0:len(i)] == i:
                if self.wordBreak1(s[len(i):], wordDict):
                    return True

        return False

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [True]
        for i in xrange(1, len(s) + 1):
            dp += any(dp[j] and s[j:i] in wordDict for j in range(i)),
        return dp[-1]


if __name__ == '__main__':
    print Solution().wordBreak("aaaaaaa", ["aa", "aaaa", "code"])

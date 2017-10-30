# Word Break II


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [True]
        for i in xrange(1, len(s) + 1):
            dp += any(dp[j] and s[j:i] in wordDict for j in range(i)),
        if dp[-1]:
            dp = [[]]
            for i in xrange(1, len(s) + 1):
                k = False
                dp.append([])
                for j in xrange(i):

                    if dp[j] != [] or j == 0:
                        if s[j:i] in wordDict:
                            if j == 0:
                                dp[-1].append([i])
                            else:
                                for l in dp[j]:
                                    dp[-1].append(l + [i])
                            k = True

                if not k:
                    dp[-1] = []

            ans = []
            for i in dp[-1]:
                temp = 0
                ans.append("")
                for j in i:
                    ans[-1] += s[temp:j] + " "
                    temp = j
                ans[-1] = ans[-1][:-1]

            return ans

        else:
            return []

    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        memo = {len(s): ['']}

        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in range(i + 1, len(s) + 1)
                           if s[i:j] in wordDict
                           for tail in sentences(j)]
            return memo[i]
        return sentences(0)


if __name__ == '__main__':
    print Solution().wordBreak1("catsanddog", ["cat", "cats", "and", "sand", "dog"])

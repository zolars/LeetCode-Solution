# Edit Distance


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = []
        for i in xrange(len(word2) + 1):
            dp.append([0 for i in xrange(len(word1) + 1)])

        for i in xrange(len(word1) + 1):
            dp[0][i] = i
        for i in xrange(len(word2) + 1):
            dp[i][0] = i

        for i in dp:
            print i

        for i in xrange(1, len(word2) + 1):
            for j in xrange(1, len(word1) + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1,  # replace
                                   dp[i - 1][j] + 1,  # insert
                                   dp[i][j - 1] + 1  # delete
                                   )

        print "\n---\n"
        for i in dp:
            print i

        print "\n---\n"

        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().minDistance("abcd", "ed"))

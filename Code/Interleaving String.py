# Interleaving String


class Solution(object):
    def isInterleave1(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if s1 == '' and s2 == '' and s3 == '':
            return True
        elif s1 + s2 + s3 == s1 + s2 and s1 + s2 + s3 == s3:
            return False

        else:
            if s1 != "" and s3 != "":
                if s3[0] == s1[0]:
                    if self.isInterleave1(s1[1:], s2, s3[1:]):
                        return True

            if s2 != "" and s3 != "":
                if s3[0] == s2[0]:
                    if self.isInterleave1(s1, s2[1:], s3[1:]):
                        return True

        return False

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2):
            return False

        dp = [[0 for j in xrange(len(s2) + 1)]for i in xrange(len(s1) + 1)]
        print dp

        for i in xrange(len(s1) + 1):
            for j in xrange(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and (s2[j - 1] == s3[i + j - 1])
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and (s1[i - 1] == s3[i + j - 1])
                else:
                    dp[i][j] = (dp[i][j - 1] and (s2[j - 1] == s3[i + j - 1])
                                ) or (dp[i - 1][j] and (s1[i - 1] == s3[i + j - 1]))

        return dp[-1][-1]


if __name__ == '__main__':
    print Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")

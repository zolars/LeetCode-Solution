# Scramble String
# -*- coding: utf-8 -*-


class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):

        if not s1 or not s2 or len(s1) != len(s2):
            return False
        if s1 == s2:
            return True

        l = len(s1)

        ans = [[[False for j in xrange(l)] for i in xrange(l)]
               for n in xrange(l + 1)]

        for i in xrange(l):
            for j in xrange(l):
                if s1[i] == s2[j]:
                    ans[1][i][j] = True

        for n in xrange(2, l + 1):
            for i in xrange(l - n + 1):
                for j in xrange(l - n + 1):
                    for k in xrange(1, n):

                        if (ans[k][i][j] and ans[n - k][i + k][j + k]) or (ans[k][i][j + n - k] and ans[n - k][i + k][j]):
                            ans[n][i][j] = True

                        # 状态转移方程:
                        # (ans[k][i][j] and ans[n - k][i + k][j + k])
                        # or
                        # (ans[k][i][j + n - k] and ans[n - k][i + k][j])
                        # 从i, j开始, 在其后寻找n个元素
                        # 将(i, i+n), (j, j+n)的遍历分割为双区间
                        # 图例:
                        # ----------------------------------------------
                        # [1]:
                        # 1   2   3   4   5   6   7   8   9  10 11 12 13
                        #     i       i+k             i+n
                        #                 j       j+k             j+n
                        #
                        # [2]:
                        # 1   2   3   4   5   6   7   8   9  10 11 12 13
                        #     i       i+k             i+n
                        #                 i               j+n-k   i+n
                        #
                        # ----------------------------------------------

                            break

        for i in ans:
            print "---"
            for j in i:
                print " ", j, " "
                print

        return ans[n][0][0]


if __name__ == "__main__":
    s1, s2 = "great", "rgtae"
    print Solution().isScramble(s1, s2)

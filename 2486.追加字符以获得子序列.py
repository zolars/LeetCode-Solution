#
# @lc app=leetcode.cn id=2486 lang=python3
#
# [2486] 追加字符以获得子序列
#

# @lc code=start
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        i, j = 0, 0
        while i < m and j < n:
            if s[i] == t[j]:
                j += 1
            i += 1
        return n - j


# @lc code=end

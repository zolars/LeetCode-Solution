#
# @lc app=leetcode.cn id=1869 lang=python3
#
# [1869] 哪种连续子字符串更长
#

# @lc code=start
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        n = len(s)
        max0 = max1 = i = 0
        while i < n:
            start = i
            i += 1
            while i < n and s[i] == s[start]:
                i += 1
            if s[start] == "0":
                max0 = max(max0, i - start)
            else:
                max1 = max(max1, i - start)
        return max1 > max0


# @lc code=end

#
# @lc app=leetcode.cn id=3456 lang=python3
#
# [3456] 找出长度为 K 的特殊子字符串
#

# @lc code=start
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        i = 0
        while i < n:
            start = i
            i += 1
            while i < n and s[i] == s[i - 1]:
                i += 1
            if i - start == k:
                return True
        return False


# @lc code=end

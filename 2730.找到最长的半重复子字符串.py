#
# @lc app=leetcode.cn id=2730 lang=python3
#
# [2730] 找到最长的半重复子字符串
#

# @lc code=start
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        ans = 0
        left = 0
        already_flag = -1
        for right, c in enumerate(s):
            if right == 0:
                continue
            if c == s[right - 1]:
                if already_flag == -1:
                    already_flag = right
                else:
                    left = already_flag
                    already_flag = right
            ans = max(ans, right - left + 1)
        return ans


# @lc code=end

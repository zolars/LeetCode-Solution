#
# @lc app=leetcode.cn id=1208 lang=python3
#
# [1208] 尽可能使字符串相等
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = 0
        cost = 0
        left = 0
        for right, c in enumerate(s):
            cost += abs(ord(c) - ord(t[right]))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)

        return ans


# @lc code=end

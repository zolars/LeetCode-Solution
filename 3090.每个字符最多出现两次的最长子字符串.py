#
# @lc app=leetcode.cn id=3090 lang=python3
#
# [3090] 每个字符最多出现两次的最长子字符串
#

# @lc code=start
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        result = 0
        stock = {}
        left = 0
        for right, c in enumerate(s):
            if c in stock:
                stock[c] += 1
            else:
                stock[c] = 1
            while stock[c] > 2:
                stock[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result


# @lc code=end

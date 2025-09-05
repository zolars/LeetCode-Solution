#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        stock = set()
        for right, c in enumerate(s):
            if c in stock:
                max_length = max(max_length, right - left)
                while c in stock:
                    stock.remove(s[left])
                    left += 1
            stock.add(c)
        max_length = max(max_length, len(s) - left)
        return max_length


# @lc code=end

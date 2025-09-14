#
# @lc app=leetcode.cn id=2904 lang=python3
#
# [2904] 最短且字典序最小的美丽子字符串
#

# @lc code=start
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""
        ones = []
        for i, c in enumerate(s):
            if c == "1":
                ones += [i]
        ans = "1" * len(s)
        ans_length = len(s)
        for i in range(len(ones) - k + 1):
            current = s[ones[i] : ones[i + k - 1] + 1]
            length = ones[i + k - 1] - ones[i] + 1
            if length < ans_length:
                ans = current
                ans_length = length
            elif length == ans_length:
                ans = current if current < ans else ans
        return ans


# @lc code=end

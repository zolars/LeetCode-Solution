#
# @lc app=leetcode.cn id=2414 lang=python3
#
# [2414] 最长的字母序连续子字符串的长度
#

# @lc code=start
class Solution:
    # ord(char) 将字母转为 ASCII/Unicode 整数
    # chr(code) 将整数转为字母
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        ans = i = 0
        while i < n:
            start = i
            i += 1
            while i < n and ord(s[i]) == ord(s[i - 1]) + 1:
                i += 1
            ans = max(ans, i - start)
        return ans


# @lc code=end

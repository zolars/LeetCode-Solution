#
# @lc app=leetcode.cn id=2109 lang=python3
#
# [2109] 向字符串添加空格
#

# @lc code=start
class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        ans = ""
        left = 0
        for i in spaces:
            ans += s[left:i] + " "
            left = i
        ans += s[left:]
        return ans


# @lc code=end

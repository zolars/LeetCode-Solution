#
# @lc app=leetcode.cn id=1759 lang=python3
#
# [1759] 统计同质子字符串的数目
#

# @lc code=start
class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = i = 0
        n = len(s)
        while i < n:
            start = i
            i += 1
            while i < n and s[i] == s[i - 1]:
                i += 1
            ans += (i - start) * (i - start + 1) // 2
        return ans % (10**9 + 7)


# @lc code=end

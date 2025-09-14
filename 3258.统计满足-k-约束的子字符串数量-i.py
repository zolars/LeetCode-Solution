#
# @lc app=leetcode.cn id=3258 lang=python3
#
# [3258] 统计满足 K 约束的子字符串数量 I
#

# @lc code=start
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        length = len(s)
        ans = length * (length + 1) // 2
        left = 0
        current_0 = current_1 = 0
        for right, c in enumerate(s):
            if c == "0":
                current_0 += 1
            else:
                current_1 += 1
            while current_0 > k and current_1 > k:
                ans -= length - right
                if s[left] == "0":
                    current_0 -= 1
                else:
                    current_1 -= 1
                left += 1
        return ans


# @lc code=end

#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math

        i, j = 0, math.isqrt(c)
        while i <= j:
            current = i**2 + j**2
            if current == c:
                return True
            elif current < c:
                i += 1
            else:
                j -= 1
        return False


# @lc code=end

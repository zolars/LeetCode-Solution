#
# @lc app=leetcode.cn id=2310 lang=python3
#
# [2310] 个位数字为 K 的整数之和
#

# @lc code=start
class Solution:
    # (1, num + 1) 是超级关键
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        for i in range(1, num + 1):
            if (num - i * k) >= 0 and (num - i * k) % 10 == 0:
                return i
        return -1


# @lc code=end

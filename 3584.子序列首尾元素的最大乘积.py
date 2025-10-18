#
# @lc app=leetcode.cn id=3584 lang=python3
#
# [3584] 子序列首尾元素的最大乘积
#
from math import inf


# @lc code=start
class Solution:
    # 找任意大小为 m 的子序列中首尾元素
    # 这不就是 j - i + 1 >= m
    def maximumProduct(self, nums: list[int], m: int) -> int:
        ans = mx = -inf
        mn = inf
        i = 0
        for x in nums[m - 1 :]:
            y = nums[i]
            mx = max(mx, y)
            mn = min(mn, y)
            ans = max(ans, x * mx, x * mn)
            i += 1
        return int(ans)


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.maximumProduct(
        nums=[2, -1, 2, -6, 5, 2, -5, 7],
        m=2,
    )
    print(ans)

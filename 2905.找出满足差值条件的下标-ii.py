#
# @lc app=leetcode.cn id=2905 lang=python3
#
# [2905] 找出满足差值条件的下标 II
#
from math import inf


# @lc code=start
class Solution:
    def findIndices(
        self,
        nums: list[int],
        indexDifference: int,
        valueDifference: int,
    ) -> list[int]:
        mx = -inf
        mx_idx = 0
        mn = inf
        mn_idx = 0

        for idx, num in enumerate(nums[indexDifference:]):
            if nums[idx] > mx:
                mx = nums[idx]
                mx_idx = idx
            if nums[idx] < mn:
                mn = nums[idx]
                mn_idx = idx
            if abs(mx - num) >= valueDifference:
                return [idx + indexDifference, mx_idx]
            if abs(mn - num) >= valueDifference:
                return [idx + indexDifference, mn_idx]
        return [-1, -1]


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.findIndices(
        nums=[1, 2, 3],
        indexDifference=2,
        valueDifference=4,
    )
    print(ans)

#
# @lc app=leetcode.cn id=795 lang=python3
#
# [795] 区间子数组个数
#

# @lc code=start
class Solution:
    # # 时间复杂度为2n的算法
    # def numSubarrayBoundedMax(
    #     self,
    #     nums: list[int],
    #     left: int,
    #     right: int,
    # ) -> int:
    #     def count(upper):
    #         res = 0
    #         n = len(nums)
    #         i, j = 0, 0
    #         while j < n:
    #             while j < n and nums[j] <= upper:
    #                 j += 1
    #             res += (j - i) * (j - i + 1) // 2
    #             i = j + 1
    #             j += 1
    #         return res

    #     return count(right) - count(left - 1)

    def numSubarrayBoundedMax(
        self,
        nums: list[int],
        left: int,
        right: int,
    ) -> int:
        ans = 0
        i0, i1 = -1, -1
        for i, num in enumerate(nums):
            if num > right:
                i0 = i
            if num >= left:
                i1 = i
            ans += i1 - i0
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.numSubarrayBoundedMax(
        nums=[2, 9, 2, 5, 6],
        left=2,
        right=8,
    )
    print(ans)

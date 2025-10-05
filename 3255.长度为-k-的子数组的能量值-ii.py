#
# @lc app=leetcode.cn id=3255 lang=python3
#
# [3255] 长度为 K 的子数组的能量值 II
#

# @lc code=start
class Solution:
    # TODO: 特判的情况好乱
    def resultsArray(
        self,
        nums: list[int],
        k: int,
    ) -> list[int]:
        i = 0
        n = len(nums)
        if k <= 1:
            return nums
        while i < n:
            start = i
            i += 1
            while i < n and nums[i] == nums[i - 1] + 1:
                i += 1
            if i - start < k:
                nums[start:i] = [-1] * (i - start)
            else:
                nums[start:i] = [-1] * (k - 1) + nums[start + k - 1 : i]
        return nums[k - 1 :]


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.resultsArray(
        [52, 12, 13, 14, 15, 16],
        3,
    )
    print(ans)

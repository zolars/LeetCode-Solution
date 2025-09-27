#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
class Solution:
    # TODO: 挺简单的双指针写半天
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n = len(nums)
        i = 0
        j = 1
        while i < n - 1 or j < n:
            while i < n - 1 and nums[i] % 2 == 0:
                i += 2
            while j < n and nums[j] % 2 == 1:
                j += 2
            if i < n - 1 and j < n:
                nums[i], nums[j] = nums[j], nums[i]

        return nums


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.sortArrayByParityII([4, 2, 5, 7])
    print(ans)

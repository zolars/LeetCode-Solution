#
# @lc app=leetcode.cn id=2460 lang=python3
#
# [2460] 对数组执行操作
#

# @lc code=start
class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        left = 0
        for right in range(n):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.applyOperations([0, 1])
    print(ans)

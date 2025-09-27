#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        left = 0
        for num in nums[1:]:
            if num != nums[left]:
                left += 1
                nums[left] = num
        return left + 1


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.removeDuplicates([1, 2, 3, 4])
    print(ans)

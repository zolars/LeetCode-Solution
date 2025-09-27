#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    # TODO: 与正确答案擦肩而过
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        left = 2
        for num in nums[2:]:
            if num != nums[left - 2]:
                nums[left] = num
                left += 1
        return left


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])
    print(ans)

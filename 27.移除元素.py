#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        i, j = 0, n - 1
        while i < j:
            if nums[i] != val:
                i += 1
            elif nums[j] == val:
                j -= 1
            else:
                nums[i] = nums[j]
                i += 1
                j -= 1
        if nums[j] == val:
            return j
        else:
            return j + 1


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.removeElement([3, 3, 3, 3], 3)
    print(ans)

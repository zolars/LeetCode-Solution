#
# @lc app=leetcode.cn id=2875 lang=python3
#
# [2875] 无限数组的最短子数组
#

# @lc code=start
class Solution:
    def minSizeSubarray(self, nums: list[int], target: int) -> int:
        ans = 10**9 + 1
        amount = sum(nums)
        ans_plus = len(nums) * (target // amount)
        less = target % amount
        if less == 0:
            return ans_plus
        current = target - less
        nums = nums * 2
        left = 0
        for right, num in enumerate(nums):
            current += num
            while current >= target and left <= right:
                if current == target:
                    ans = min(ans, ans_plus + right - left + 1)
                current -= nums[left]
                left += 1
        if ans == 10**9 + 1:
            return -1
        else:
            return ans


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    ans = sol.minSizeSubarray([1, 1, 1], 1000000000)
    print(ans)

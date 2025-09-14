#
# @lc app=leetcode.cn id=930 lang=python3
#
# [930] 和相同的二元子数组
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        ans = current0 = current1 = left0 = left1 = 0
        for right, num in enumerate(nums):
            current0 += num
            current1 += num
            while current0 >= goal and left0 <= right:
                current0 -= nums[left0]
                left0 += 1
            while current1 > goal and left1 <= right:
                current1 -= nums[left1]
                left1 += 1
            if current1 == goal:
                ans += left0 - left1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.numSubarraysWithSum(
        [1, 0, 1, 0, 1],
        3,
    )
    print(ans)

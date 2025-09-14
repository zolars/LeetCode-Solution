#
# @lc app=leetcode.cn id=2962 lang=python3
#
# [2962] 统计最大元素出现至少 K 次的子数组
#

# @lc code=start
class Solution:
    # 仍然是大道至简
    def countSubarrays(self, nums: list[int], k: int) -> int:
        ans = 0
        max_num = max(nums)
        left = 0
        current = 0
        for num in nums:
            current += 1 if num == max_num else 0
            while current >= k:
                current -= 1 if nums[left] == max_num else 0
                left += 1
            ans += left
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.countSubarrays([1, 4, 2, 3, 3], 2)

#
# @lc app=leetcode.cn id=1248 lang=python3
#
# [1248] 统计「优美子数组」
#

# @lc code=start
class Solution:
    # 恰好型滑动窗口可以死记硬背
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        ans = left0 = left1 = current0 = current1 = 0
        for right, num in enumerate(nums):
            if num % 2 == 1:
                current0 += 1
                current1 += 1
            while current0 >= k and left0 <= right:
                if nums[left0] % 2 == 1:
                    current0 -= 1
                left0 += 1
            while current1 > k and left1 <= right:
                if nums[left1] % 2 == 1:
                    current1 -= 1
                left1 += 1
            if current1 == k:
                ans += left0 - left1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.numberOfSubarrays(
        nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
        k=2,
    )
    print(ans)

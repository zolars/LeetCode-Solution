#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        ans = 0
        n = len(nums)
        nums.sort()
        diff = 10**5
        for left, num in enumerate(nums):
            i, j, k = left + 1, n - 1, target - num
            current = 0
            while i < j:
                current = nums[i] + nums[j]
                if current == k:
                    return target
                elif current < k:
                    i += 1
                elif current > k:
                    j -= 1
                cc = abs(current - k)
                if cc < diff:
                    diff = cc
                    ans = num + current
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.threeSumClosest(
        [-1000, -1000, -1000],
        10000,
    )
    print(ans)

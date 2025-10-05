#
# @lc app=leetcode.cn id=2765 lang=python3
#
# [2765] 最长交替子数组
#

# @lc code=start
class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        ans = -1
        i = 0
        n = len(nums)
        while i < n - 1:
            start = i
            flag = 1
            while i < n - 1 and nums[i + 1] == nums[i] + flag:
                flag *= -1
                i += 1
            if i != start:
                ans = max(ans, i - start + 1)
            else:
                i += 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.alternatingSubarray([2, 5, 7])
    print(ans)

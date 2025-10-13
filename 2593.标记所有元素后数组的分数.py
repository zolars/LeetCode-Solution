#
# @lc app=leetcode.cn id=2593 lang=python3
#
# [2593] 标记所有元素后数组的分数
#

# @lc code=start
class Solution:
    # TODO: 没那么难，先模拟清楚了
    def findScore(self, nums: list[int]) -> int:
        ans = i = 0
        n = len(nums)
        while i < n:
            start = i
            i += 1
            while i < n and nums[i] < nums[i - 1]:
                i += 1
            ans += nums[i - 1]
            j = i - 1
            while True:
                j -= 2
                if j >= start:
                    ans += nums[j]
                else:
                    break
            i += 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.findScore(
        [10, 44, 10, 8, 48, 30, 17, 38, 41, 27, 16, 33, 45, 45, 34, 30, 22, 3, 42, 42]
    )
    print(ans)

#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        minn, maxx = nums[n - 1], nums[0]
        begin, end = 0, -1
        for i, num in enumerate(nums):
            if num < maxx:
                end = i
            else:
                maxx = num
        for i, num in enumerate(nums[::-1]):
            i = n - i - 1
            if num > minn:
                begin = i
            else:
                minn = num
        return end - begin + 1


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.findUnsortedSubarray(
        [1, 12, 2, 11],
    )
    print(ans)

#
# @lc app=leetcode.cn id=2563 lang=python3
#
# [2563] 统计公平数对的数目
#

# @lc code=start
class Solution:
    # # TODO: 两次双向双指针做法
    # def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
    #     nums.sort()

    #     def count(upper):
    #         ans = 0
    #         i, j = 0, len(nums) - 1
    #         while i < j:
    #             current = nums[i] + nums[j]
    #             if current <= upper:
    #                 ans += j - i
    #                 i += 1
    #             else:
    #                 j -= 1
    #         return ans

    #     return count(upper) - count(lower - 1)

    # TODO: 三指针, 看不懂
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        ans = 0
        n = len(nums)
        nums.sort()
        right1 = right2 = n
        for left, num in enumerate(nums):
            while right2 and num + nums[right2 - 1] > upper:
                right2 -= 1
            while right1 and num + nums[right1 - 1] >= lower:
                right1 -= 1
            print(left, right1, right2, min(left, right2) - min(left, right1))
            ans += min(left, right2) - min(left, right1)
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.countFairPairs(
        nums=[0, 1, 4, 4, 5, 7],
        lower=3,
        upper=6,
    )
    print(ans)

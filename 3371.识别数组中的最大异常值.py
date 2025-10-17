#
# @lc app=leetcode.cn id=3371 lang=python3
#
# [3371] 识别数组中的最大异常值
#

# @lc code=start
class Solution:
    def getLargestOutlier(self, nums: list[int]) -> int:
        ans = -1001
        sum_nums = sum(nums)
        hash_nums = {}
        for num in nums:
            if num in hash_nums:
                hash_nums[num] += 1
            else:
                hash_nums[num] = 1
        for num in nums:
            current = sum_nums - num
            if (
                current % 2 == 0
                and current // 2 in hash_nums
                and (current // 2 != num or hash_nums[num] >= 2)
            ):
                if num > ans:
                    ans = num
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.getLargestOutlier([6, -31, 50, -35, 41, 37, -42, 13])
    print(ans)

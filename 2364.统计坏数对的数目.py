#
# @lc app=leetcode.cn id=2364 lang=python3
#
# [2364] 统计坏数对的数目
#

# @lc code=start
class Solution:
    # 数学变换
    def countBadPairs(self, nums: list[int]) -> int:
        n = len(nums)
        ans = n * (n - 1) // 2
        stock = {}
        for idx, num in enumerate(nums):
            if num - idx in stock:
                ans -= stock[num - idx]
                stock[num - idx] += 1
            else:
                stock[num - idx] = 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.countBadPairs(nums=[4, 1, 3, 3])
    print(ans)

#
# @lc app=leetcode.cn id=1679 lang=python3
#
# [1679] K 和数对的最大数目
#
from collections import defaultdict


# @lc code=start
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        ans = 0
        stock = defaultdict(int)
        for num in nums:
            numm = k - num
            if stock[numm] > 0:
                ans += 1
                stock[numm] -= 1
            else:
                stock[num] += 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxOperations([1, 2, 3, 4], 5)
    print(ans)

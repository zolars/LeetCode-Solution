#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#

# @lc code=start
from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        ans = 0
        stock = defaultdict(int)
        for num in nums:
            ans += stock[num]
            stock[num] += 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.numIdenticalPairs([1, 1, 1, 1])
    print(ans)

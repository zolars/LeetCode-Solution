#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
from collections import defaultdict


# @lc code=start
class Solution:
    def containsNearbyDuplicate(
        self,
        nums: list[int],
        k: int,
    ) -> bool:
        stock = defaultdict(int)
        for idx, num in enumerate(nums):
            if num in stock and idx - stock[num] <= k:
                return True
            else:
                stock[num] = idx
        return False


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.containsNearbyDuplicate([1, 2, 3, 1], 3)
    print(ans)

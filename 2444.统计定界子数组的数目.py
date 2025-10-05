#
# @lc app=leetcode.cn id=2444 lang=python3
#
# [2444] 统计定界子数组的数目
#

# @lc code=start
class Solution:
    # TODO: 记住五个字：枚举右端点
    def countSubarrays(
        self,
        nums: list[int],
        minK: int,
        maxK: int,
    ) -> int:
        ans, minI, maxI, i0 = 0, -1, -1, -1
        for i, num in enumerate(nums):
            if num == minK:
                minI = i
            if num == maxK:
                maxI = i
            if num < minK or num > maxK:
                i0 = i
                minI = i
                maxI = i
            ans += min(minI, maxI) - i0
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.countSubarrays(
        [1, 1, 1, 1],
        1,
        1,
    )
    print(ans)

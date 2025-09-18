#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        ans = bns = 0
        n = len(height)

        i, j = 0, n - 1
        while i < j:
            bns = (j - i) * min(height[i], height[j])
            ans = max(ans, bns)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(ans)

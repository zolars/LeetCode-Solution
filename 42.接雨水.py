#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    # O(2n)
    def trap(self, height: list[int]) -> int:
        ans = i = 0
        n = len(height)
        max_idx, _ = max(enumerate(height), key=lambda x: x[1])
        while i < max_idx:
            start = i
            while i < n and height[i] <= height[start]:
                ans += height[start] - height[i]
                i += 1
        i = n - 1
        while i > max_idx:
            start = i
            while i > max_idx and height[i] <= height[start]:
                ans += height[start] - height[i]
                i -= 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(ans)

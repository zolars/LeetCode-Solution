#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    # TODO: 完全不会做
    def trap(self, height: list[int]) -> int:
        ans = left_bns = right_bns = 0
        i, j = 0, len(height) - 1
        while i < j:
            left_bns = max(left_bns, height[i])
            right_bns = max(right_bns, height[j])
            if left_bns < right_bns:
                ans += left_bns - height[i]
                i += 1
            else:
                ans += right_bns - height[j]
                j -= 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(ans)

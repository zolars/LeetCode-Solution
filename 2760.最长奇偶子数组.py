#
# @lc app=leetcode.cn id=2760 lang=python3
#
# [2760] 最长奇偶子数组
#

# @lc code=start
class Solution:
    def longestAlternatingSubarray(
        self,
        nums: list[int],
        threshold: int,
    ) -> int:
        n = len(nums)
        ans = i = 0
        while i < n:
            # 直接跳过
            if nums[i] > threshold or nums[i] % 2 == 1:
                i += 1
                continue
            start = i  # 记录这一组的开始位置
            i += 1  # 开始位置已经满足要求，从下一个位置开始判断
            while i < n and nums[i] <= threshold and nums[i] % 2 != nums[i - 1] % 2:
                i += 1
            # 从 start 到 i - 1 是满足题目要求的（并且无法再延长的）子数组
            ans = max(ans, i - start)
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.longestAlternatingSubarray(
        nums=[4, 10, 3],
        threshold=10,
    )
    print(ans)

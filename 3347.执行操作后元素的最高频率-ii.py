#
# @lc app=leetcode.cn id=3347 lang=python3
#
# [3347] 执行操作后元素的最高频率 II
#

# @lc code=start
class Solution:
    # TODO: 这题真是集大成者了
    # 如果 x 在 nums 中，用同向三指针计算。
    # 如果 x 不在 nums 中，用滑动窗口计算。
    def maxFrequency(
        self,
        nums: list[int],
        k: int,
        numOperations: int,
    ) -> int:
        ans = 0
        n = len(nums)
        nums.sort()
        cnt, left, right = 0, 0, 0
        for x, num in enumerate(nums):
            cnt += 1
            if x != n - 1 and nums[x + 1] == num:
                continue
            while nums[left] < num - k:
                left += 1
            while right < n and nums[right] <= num + k:
                right += 1
            # cnt + numOperations: 把操作拉满也就能整出来这么多了
            ans = max(ans, min(right - left, cnt + numOperations))
            cnt = 0

        if ans >= numOperations:
            return ans

        left = 0
        for right, num in enumerate(nums):
            while nums[left] < num - k * 2:
                left += 1
            ans = max(ans, right - left + 1)

        return min(ans, numOperations)


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxFrequency(
        [5, 11, 20, 20],
        5,
        1,
    )
    print(ans)

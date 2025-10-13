#
# @lc app=leetcode.cn id=2948 lang=python3
#
# [2948] 交换得到字典序最小的数组
#

# @lc code=start
class Solution:
    # TODO: 不要怕，就带着下标循环
    def lexicographicallySmallestArray(
        self,
        nums: list[int],
        limit: int,
    ) -> list[int]:
        i = 0
        n = len(nums)
        nums_with_idx = [(num, idx) for idx, num in enumerate(nums)]
        sorted_nums = sorted(nums_with_idx)
        while i < n:
            start = i
            i += 1
            while i < n and sorted_nums[i][0] - sorted_nums[i - 1][0] <= limit:
                i += 1
            sub = sorted_nums[start:i]
            idxs = sorted([idx for _, idx in sub])
            for j, idx in enumerate(idxs):
                nums[idx] = sorted_nums[start + j][0]
        return nums


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.lexicographicallySmallestArray(
        nums=[1, 7, 6, 18, 2, 1],
        limit=3,
    )
    print(ans)

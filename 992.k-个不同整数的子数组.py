#
# @lc app=leetcode.cn id=992 lang=python3
#
# [992] K 个不同整数的子数组
#

# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        ans = left0 = left1 = current0 = current1 = 0
        stock0 = {}
        stock1 = {}
        for right, num in enumerate(nums):
            if num in stock0:
                stock0[num] += 1
                if stock0[num] == 1:
                    current0 += 1
            else:
                stock0[num] = 1
                current0 += 1
            if num in stock1:
                stock1[num] += 1
                if stock1[num] == 1:
                    current1 += 1
            else:
                stock1[num] = 1
                current1 += 1
            while current0 > k and left0 <= right:
                stock0[nums[left0]] -= 1
                if stock0[nums[left0]] == 0:
                    current0 -= 1
                left0 += 1
            while current1 >= k and left1 <= right:
                stock1[nums[left1]] -= 1
                if stock1[nums[left1]] == 0:
                    current1 -= 1
                left1 += 1
            ans += left1 - left0
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.subarraysWithKDistinct(
        nums=[1, 2, 1, 3, 4, 1, 2, 1, 3, 4, 5, 1, 2, 3],
        k=3,
    )
    print(ans)

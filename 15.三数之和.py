#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    # 看起来笨，但是能过
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()

        def twoSum(arr, k):
            res = []
            i, j = 0, len(arr) - 1
            while i < j:
                current = arr[i] + arr[j]
                if current < k:
                    i += 1
                elif current > k:
                    j -= 1
                else:
                    res.append([arr[i], arr[j]])
                    while arr[i + 1] == arr[i] and i < len(arr) - 2:
                        i += 1
                    i += 1
            return res

        left = 0
        while left < len(nums) - 1:
            res = twoSum(nums[left + 1 :], -nums[left])
            if res:
                for r in res:
                    ans.append([nums[left]] + r)
            while nums[left + 1] == nums[left] and left < len(nums) - 2:
                left += 1
            left += 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.threeSum([-1, 0, 1, 2, -1, -4])
    print(ans)

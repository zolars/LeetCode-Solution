#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    # TODO: 四次剪枝
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for left1, num1 in enumerate(nums[:-3]):
            # 剪枝
            if num1 + nums[left1 + 1] + nums[left1 + 2] + nums[left1 + 3] > target:
                break
            # 剪枝
            if num1 + nums[-3] + nums[-2] + nums[-1] < target:
                continue
            for left2, num2 in enumerate(nums[left1 + 1 : -2]):
                # 剪枝
                if num1 + num2 + nums[left2 + 1] + nums[left2 + 2] > target:
                    break
                # 剪枝
                if num1 + num2 + nums[-2] + nums[-1] < target:
                    continue
                i, j, k = left1 + 1 + left2 + 1, n - 1, target - num1 - num2
                while i < j:
                    current = nums[i] + nums[j]
                    if current < k:
                        i += 1
                    elif current > k:
                        j -= 1
                    else:
                        append_flag = True
                        for oneans in ans:
                            if oneans == [num1, num2, nums[i], nums[j]]:
                                append_flag = False
                                break
                        if append_flag:
                            ans.append([num1, num2, nums[i], nums[j]])
                        i += 1
                        j -= 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.fourSum(
        [-4, -3, -2, -1],
        -10,
    )
    print(ans)

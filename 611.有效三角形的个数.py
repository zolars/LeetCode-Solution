#
# @lc app=leetcode.cn id=611 lang=python3
#
# [611] 有效三角形的个数
#

# @lc code=start
class Solution:
    # 任意两边之和大于第三边
    # TODO: 两次剪枝
    def triangleNumber(self, nums: list[int]) -> int:
        ans = 0
        nums.sort()
        n = len(nums)
        k = n - 1
        while k > 1:
            # 剪枝
            if nums[k - 2] + nums[k - 1] <= nums[k]:
                pass
            # 剪枝
            elif nums[0] + nums[1] > nums[k]:
                ans += k * (k - 1) // 2
            else:
                i, j = 0, k - 1
                while i < j:
                    if nums[i] + nums[j] > nums[k]:
                        ans += j - i
                        j -= 1
                    else:
                        i += 1
            k -= 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.triangleNumber([2, 2, 2, 3])
    print(ans)

#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            current = numbers[i] + numbers[j]
            if current == target:
                return [i + 1, j + 1]
            elif current > target:
                j -= 1
            else:
                i += 1
        return []


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.twoSum(
        [-1, 0],
        -1,
    )
    print(ans)

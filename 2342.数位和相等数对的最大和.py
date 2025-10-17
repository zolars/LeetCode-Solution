#
# @lc app=leetcode.cn id=2342 lang=python3
#
# [2342] 数位和相等数对的最大和
#
from collections import defaultdict


# @lc code=start
class Solution:
    # TODO: 用数学方法计算位数和
    def maximumSum(self, nums: list[int]) -> int:
        ans = -1
        stock = defaultdict(int)
        for num in nums:
            digit_sum = 0
            temp = num
            while temp:
                digit_sum += temp % 10
                temp //= 10
            if digit_sum in stock:
                current_ans = num + stock[digit_sum]
                if current_ans > ans:
                    ans = current_ans
            if num > stock[digit_sum]:
                stock[digit_sum] = num

        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.maximumSum(
        nums=[
            229,
            398,
            269,
            317,
            420,
            464,
            491,
            218,
            439,
            153,
            482,
            169,
            411,
            93,
            147,
            50,
            347,
            210,
            251,
            366,
            401,
        ],
    )
    print(ans)

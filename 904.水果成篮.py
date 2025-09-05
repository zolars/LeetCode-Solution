#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        result = 0
        left = 0
        stock = {}
        for right, fruit in enumerate(fruits):
            if fruit in stock:
                stock[fruit] += 1
            else:
                stock[fruit] = 1
            while len(stock) > 2:
                stock[fruits[left]] -= 1
                if stock[fruits[left]] == 0:
                    stock.pop(fruits[left])
                left += 1
            result = max(result, right - left + 1)
        return result


# @lc code=end

#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#

# @lc code=start
class Solution:
    # TODO: 复杂度是m+n，按说可以优化到n
    # def isLongPressedName(self, name: str, typed: str) -> bool:
    #     stock_name, stock_typed = [], []
    #     for c in name:
    #         if stock_name and stock_name[-1][0] == c:
    #             stock_name[-1][1] += 1
    #         else:
    #             stock_name += [[c, 1]]
    #     for c in typed:
    #         if stock_typed and stock_typed[-1][0] == c:
    #             stock_typed[-1][1] += 1
    #         else:
    #             stock_typed += [[c, 1]]
    #     if len(stock_name) != len(stock_typed):
    #         return False
    #     for i, j in zip(stock_name, stock_typed):
    #         if i[0] != j[0] or i[1] > j[1]:
    #             return False
    #     return True

    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j, stock = 0, 0, ""
        while i < len(name) or j < len(typed):
            if j == len(typed):
                return False
            elif i < len(name) and typed[j] == name[i]:
                stock = name[i]
                i += 1
                j += 1
            elif typed[j] == stock:
                j += 1
            else:
                return False
        return True


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.isLongPressedName(
        "alexd",
        "ale",
    )
    print(ans)

#
# @lc app=leetcode.cn id=1616 lang=python3
#
# [1616] 分割两个字符串得到回文串
#

# @lc code=start
class Solution:
    # 写一个回文字符串检测函数, 好慢
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(c):
            ans = True
            i, j = 0, len(c) - 1
            while i < j:
                if c[i] == c[j]:
                    i += 1
                    j -= 1
                else:
                    ans = False
                    break
            return ans

        n = len(a)
        left_a = left_b = -1
        i, j = 0, n - 1
        while i < j and (left_a < 0 or left_b < 0):
            if a[i] != b[j] and left_a < 0:
                left_a = i
            if b[i] != a[j] and left_b < 0:
                left_b = i
            i += 1
            j -= 1
        if left_a == -1 or left_b == -1:
            return True
        left = max(left_a, left_b)
        if check(a[left : n - left]):
            return True
        elif check(b[left : n - left]):
            return True
        else:
            return False


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.checkPalindromeFormation(
        "ulacfd",
        "jizalu",
    )
    print(ans)

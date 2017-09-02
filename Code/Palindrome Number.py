class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < -2147483648 or x > 2147483647:
            return(False)

        num = str(x)
        l = len(num)

        if l % 2 == 0:
            left = l / 2 - 1
            right = l / 2
        else:
            left = right = l / 2

        while right - left + 1 <= l:
            if num[left] == num[right]:
                left -= 1
                right += 1
            else:
                return(False)
        else:
            return(True)


if __name__ == '__main__':
    print(Solution().isPalindrome(-10))

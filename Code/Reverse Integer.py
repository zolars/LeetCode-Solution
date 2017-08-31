class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        k, ss = 1, ''
        if x < 0:
            x *= -1
            k = -1

        s = str(x)

        for i in s[::-1]:
            ss += i

        ans = k * int(ss)

        if not -2147483648 <= ans <= 2147483647:
            ans = 0

        return(ans)


if __name__ == '__main__':
    print(Solution().reverse(153423))

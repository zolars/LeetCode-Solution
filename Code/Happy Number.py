class Solution(object):
    def divide(self, n):
        ans, num_str = 0, str(n)
        while num_str:
            ans += int(num_str[0]) ** 2
            num_str = num_str[1:]
        return ans

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = set()

        while 1:
            n = self.divide(n)
            if n == 1 or n % 10 == 0:
                return True
            elif n in dic:
                return False
            else:
                dic.add(n)


if __name__ == '__main__':
    print(Solution().isHappy(8))
